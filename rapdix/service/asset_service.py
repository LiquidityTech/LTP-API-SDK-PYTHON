from tokenize import String
from rapdix.model.request.asset.portfolio_detail_request import PortfolioDetailRequest
from rapdix.model.request.asset.portfolio_funds_history_request import PortfolioFundsHistoryRequest
from rapdix.model.request.asset.user_all_portfolio_request import UserAllPortfolioRequest
from rapdix.model.vo.asset.asset_portfolio_history_vo import AssetPortfolioHistoryVO
from rapdix.model.vo.asset.asset_vo import AssetVO
from ..model.page_entity import PageEntity
import json
from typing import Optional, Dict, Any, Tuple, List
from collections import OrderedDict
from rapdix.util.signature_util import SignatureUtil
from rapdix.constants.api_constants import APIConstants
from rapdix.model.response.api_response import ApiResponse
from rapdix.service.base_service import BaseService

class AssetService(BaseService):
    def portfolio_fund_history(self, request: PortfolioFundsHistoryRequest) -> Optional[ApiResponse[AssetPortfolioHistoryVO]]:
        """
        Query portfolio fund history
        
        Args:
            request: Portfolio funds history query request
        """
        url = f"{self.host}{APIConstants.ASSET_PORTFOLIO_FUNDS_HISTORY}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, AssetPortfolioHistoryVO)
    
    def portfolio_detail(self, request: PortfolioDetailRequest) -> Optional[ApiResponse[PageEntity[AssetVO]]]:
        """
        Query portfolio details
        
        Args:
            request: Portfolio detail query request
        """
        url = f"{self.host}{APIConstants.ASSET_PORTFOLIO_DETAIL}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_page_response(response_data, AssetVO)
    
    def user_all_portfolio(self, request: UserAllPortfolioRequest) -> Optional[ApiResponse[Dict[str, List[AssetVO]]]]:
        """
        Query all portfolios
        
        Args:
            request: User all portfolio query request
        """
        url = f"{self.host}{APIConstants.ASSET_ALL_PORTFOLIO}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, Dict[str, List[AssetVO]])
    
