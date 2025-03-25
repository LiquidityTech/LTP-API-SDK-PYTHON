from rapdix.model.request.position.leverage_get_request import LeverageGetRequest
from rapdix.model.request.position.leverage_set_request import LeverageSetRequest
from rapdix.model.request.position.position_close_request import PositionCloseRequest
from rapdix.model.request.position.position_portfolio_history_request import PositionPortfolioHistoryRequest
from rapdix.model.request.position.position_portfolio_request import PositionPortfolioRequest
from rapdix.model.request.position.positions_close_request import PositionsCloseRequest
from rapdix.model.vo.position.leverage_set_vo import LeverageSetVO
from rapdix.model.vo.position.leverage_vo import LeverageVO
from rapdix.model.vo.position.position_history_vo import PositionHistoryVO
from rapdix.model.vo.position.position_portfolio_vo import PositionPortfolioVO
from rapdix.model.vo.position.position_vo import PositionVO
from rapdix.model.vo.position.positions_vo import PositionsVO
from ..model.page_entity import PageEntity
import json
from typing import Optional, Dict, Any, Tuple, List
from collections import OrderedDict
from rapdix.util.signature_util import SignatureUtil
from rapdix.constants.api_constants import APIConstants
from rapdix.model.response.api_response import ApiResponse
from rapdix.service.base_service import BaseService

class PositionService(BaseService):
    def set_leverage(self, request: LeverageSetRequest) -> Optional[ApiResponse[LeverageSetVO]]:
        """
        Set leverage
        
        Args:
            request: Leverage setting request
        """
        url = f"{self.host}{APIConstants.LEVERAGE_SET}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('POST', url, param_map)
        return self._parse_response(response_data, LeverageSetVO)
    
    def get_leverage(self, request: LeverageGetRequest) -> Optional[ApiResponse[LeverageVO]]:
        """
        Get leverage
        
        Args:
            request: Leverage query request
        """
        url = f"{self.host}{APIConstants.LEVERAGE_GET}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, LeverageVO)
    
    def close_position(self, request: PositionCloseRequest) -> Optional[ApiResponse[List[PositionVO]]]:
        """
        Close position
        
        Args:
            request: Position close request
        """
        url = f"{self.host}{APIConstants.POSITION}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('DELETE', url, param_map)
        return self._parse_response(response_data, List[PositionVO])
    
    def close_positions(self, request: PositionsCloseRequest) -> Optional[ApiResponse[List[PositionsVO]]]:
        """
        Close multiple positions
        
        Args:
            request: Positions close request
        """
        url = f"{self.host}{APIConstants.POSITIONS}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('DELETE', url, param_map)
        return self._parse_response(response_data, List[PositionsVO])

    def query_portfolio(self, request: PositionPortfolioRequest) -> Optional[ApiResponse[List[PositionPortfolioVO]]]:
        """
        Query position portfolio
        
        Args:
            request: Position portfolio query request
        """
        url = f"{self.host}{APIConstants.POSITION_PORTFOLIO}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, List[PositionPortfolioVO])
    
    def query_portfolio_history(self, request: PositionPortfolioHistoryRequest) -> Optional[ApiResponse[PageEntity[PositionHistoryVO]]]:
        """
        Query position history
        
        Args:
            request: Position history query request
        """
        url = f"{self.host}{APIConstants.POSITION_HISTORY}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, PositionHistoryVO)
