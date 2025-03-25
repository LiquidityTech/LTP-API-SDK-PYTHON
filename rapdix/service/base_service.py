import json
from typing import Optional, Dict, Any, Tuple, TypeVar, Type, List, get_origin, get_args
import requests # type: ignore
from collections import OrderedDict
from rapdix.util.signature_util import SignatureUtil
from rapdix.model.response.api_response import ApiResponse
from rapdix.model.page_entity import PageEntity

T = TypeVar('T')

class BaseService:
    def __init__(self, host: str, api_key: str, secret_key: str):
        """
        Initialize base service
        
        Args:
            host: API host address
            api_key: API key
            secret_key: Secret key
        """
        self.host = host.rstrip('/')
        self.api_key = api_key
        self.secret_key = secret_key
        self.timeout = 5.0

    def _prepare_request(self, param_map: Dict) -> Tuple[str, Dict]:
        """Prepare request headers and signature"""
        nonce = SignatureUtil.gmt_now()
        sign = SignatureUtil.get_sign(param_map, self.secret_key, nonce)
        
        headers = {
            "Content-Type": "application/json",
            "nonce": nonce,
            "signature": sign,
            "X-MBX-APIKEY": self.api_key,
            "User-Agent": "Python/RapidX-SDK"
        }
        
        return nonce, headers

    def _handle_response(self, response: requests.Response) -> Optional[Dict[str, Any]]:
        """Handle response"""
        if response.status_code == 429:
            return {
                "code": 429,
                "message": "Too Many Request",
                "data": None
            }
        return response.json()

    def _make_request(self, method: str, url: str, param_map: Dict) -> Optional[Dict[str, Any]]:
        """
        Send request
        
        Args:
            method: Request method ('GET', 'POST', 'PUT', 'DELETE')
            url: Request URL
            param_map: Request parameters
            
        Returns:
            Response data
        """
        try:
            nonce, headers = self._prepare_request(param_map)
            
            if method == 'GET':
                payload = SignatureUtil.get_payload(param_map)
                if payload:
                    url = f"{url}?{payload}"
                response = requests.get(url, headers=headers, timeout=self.timeout)
            else:
                request_func = {
                    'POST': requests.post,
                    'PUT': requests.put,
                    'DELETE': requests.delete
                }.get(method)
                
                if not request_func:
                    raise ValueError(f"Unsupported HTTP method: {method}")
                    
                response = request_func(
                    url,
                    json=param_map,
                    headers=headers,
                    timeout=self.timeout,
                    verify=True
                )
            
            return self._handle_response(response)
            
        except Exception as e:
            print(f"Request error: {str(e)}")
            return None

    def _parse_response(self, response_data: Dict, response_type: Type[T]) -> ApiResponse[T]:
        """
        Parse response data
        
        Args:
            response_data: Raw response data
            response_type: Response data type
        """
        api_response = ApiResponse(
            code=response_data.get('code'),
            message=response_data.get('message'),
            data=None
        )
        
        if response_data.get('data'):
            if get_origin(response_type) is list:
                item_type = get_args(response_type)[0]
                api_response.data = [item_type(**item) for item in response_data['data']]
            elif get_origin(response_type) is dict:
                key_type, value_type = get_args(response_type)
                if get_origin(value_type) is list:
                    item_type = get_args(value_type)[0]
                    api_response.data = {
                        k: [item_type(**item) for item in v]
                        for k, v in response_data['data'].items()
                    }
                else:
                    api_response.data = response_type(**response_data['data'])
            else:
                api_response.data = response_type(**response_data['data'])
            
        return api_response

    def _parse_page_response(self, response_data: Dict, item_type: Type[T]) -> Optional[ApiResponse[PageEntity[T]]]:
        """
        Parse paginated response data
        
        Args:
            response_data: Raw response data
            item_type: List item type
        """
        if response_data:
            if response_data.get('data'):
                data = response_data['data']
                page_data = PageEntity(
                    page=data.get('page'),
                    pageSize=data.get('pageSize'),
                    pageNum=data.get('pageNum'),
                    totalSize=data.get('totalSize'),
                    list=[item_type(**item) for item in data.get('list', [])]
                )
                response_data['data'] = page_data
            return self._parse_response(response_data, PageEntity[item_type])
        return None 