from rapdix.model.request.account.account_position_request import AccountPositionModeRequest
from ..model.request.account.account_query_request import AccountQueryRequest
from ..model.vo.account.account_vo import AccountVO
from ..model.page_entity import PageEntity
import json
from typing import Optional, Dict, Any, Tuple, List
from collections import OrderedDict
from rapdix.util.signature_util import SignatureUtil
from rapdix.constants.api_constants import APIConstants
from rapdix.model.response.api_response import ApiResponse
from rapdix.service.base_service import BaseService

class AccountService(BaseService):
    def query_account(self, request: AccountQueryRequest) -> Optional[ApiResponse[List[AccountVO]]]:
        """
        Query account information
        
        Args:
            request: Account query request
        """
        url = f"{self.host}{APIConstants.ACCOUNT}"
        json_request = request.to_dict()
        response_data = self._make_request('GET', url, json_request)
        return self._parse_response(response_data, List[AccountVO])
    
    def change_account_position(self, request: AccountPositionModeRequest) -> Optional[ApiResponse[List[AccountVO]]]:
        """
        Change account position mode
        
        Args:
            request: Position mode change request
        """
        url = f"{self.host}{APIConstants.ACCOUNT}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('POST', url, param_map)
        return self._parse_response(response_data, List[AccountVO])
