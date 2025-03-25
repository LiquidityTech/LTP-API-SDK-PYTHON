import json
from typing import Optional, Dict, Any, Tuple, List
from collections import OrderedDict
from rapdix.util.signature_util import SignatureUtil
from rapdix.constants.api_constants import APIConstants
from rapdix.model.request.order.order_place_request import OrderPlaceRequest
from rapdix.model.vo.order.order_place_vo import OrderPlaceVO
from rapdix.model.response.api_response import ApiResponse
from rapdix.service.base_service import BaseService
from ..model.request.order.order_detail_request import OrderDetailRequest
from ..model.vo.order.order_vo import OrderVO
from ..model.request.order.order_cancel_request import OrderCancelRequest
from ..model.page_entity import PageEntity
from ..model.request.order.order_history_request import OrderHistoryRequest
from ..model.request.order.current_open_orders_request import CurrentOpenOrdersRequest
from ..model.request.order.order_replace_request import OrderReplaceRequest
from ..model.vo.order.order_replace_vo import OrderReplaceVO
from ..model.vo.order.order_cancel_vo import OrderCancelVO
from ..model.vo.order.order_cancels_vo import OrderCancelsVO

class OrderService(BaseService):
    def place_order(self, request: OrderPlaceRequest) -> Optional[ApiResponse[OrderPlaceVO]]:
        """
        Place an order
        
        Args:
            request: Order placement request
        """
        url = f"{self.host}{APIConstants.ORDER_PLACE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('POST', url, param_map)
        return self._parse_response(response_data, OrderPlaceVO)

    def query_order(self, request: OrderDetailRequest) -> Optional[ApiResponse[OrderVO]]:
        """
        Query order details
        
        Args:
            request: Order detail query request
        """
        url = f"{self.host}{APIConstants.ORDER}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, OrderVO)

    def cancel_order(self, request: OrderCancelRequest) -> Optional[ApiResponse[OrderCancelVO]]:
        """
        Cancel an order
        
        Args:
            request: Order cancellation request
        """
        url = f"{self.host}{APIConstants.ORDER}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('DELETE', url, param_map)
        return self._parse_response(response_data, OrderCancelVO)
    
    def cancel_orders(self, request: OrderCancelRequest) -> Optional[ApiResponse[OrderCancelsVO]]:
        """
        Cancel multiple orders
        
        Args:
            request: Order cancellation request
        """
        url = f"{self.host}{APIConstants.ORDER_CANCEL_ALL}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('DELETE', url, param_map)
        return self._parse_response(response_data, OrderCancelsVO)

    def current_open_detail(self, request: CurrentOpenOrdersRequest) -> Optional[ApiResponse[PageEntity[OrderVO]]]:
        """
        Query current open orders
        
        Args:
            request: Current open orders query request
        """
        url = f"{self.host}{APIConstants.ORDERS}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_page_response(response_data, OrderVO)

    def order_history(self, request: OrderHistoryRequest) -> Optional[ApiResponse[PageEntity[OrderVO]]]:
        """
        Query order history
        
        Args:
            request: Order history query request
        """
        url = f"{self.host}{APIConstants.ORDER_HISTORY}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_page_response(response_data, OrderVO)

    def replace_order(self, request: OrderReplaceRequest) -> Optional[ApiResponse[OrderReplaceVO]]:
        """
        Replace an order
        
        Args:
            request: Order replacement request
        """
        url = f"{self.host}{APIConstants.ORDER}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('PUT', url, param_map)
        return self._parse_response(response_data, OrderReplaceVO)

    def order_history_archive(self, request: OrderHistoryRequest) -> Optional[ApiResponse[OrderVO]]:
        """
        Query archived order history
        
        Args:
            request: Order history query request
        """
        url = f"{self.host}{APIConstants.ORDER_HISTORY_ARCHIVE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_page_response(response_data, OrderVO)

    