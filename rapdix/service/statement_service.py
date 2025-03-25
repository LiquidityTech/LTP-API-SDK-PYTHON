from rapdix.model.request.statement.statement_request import StatementRequest
from rapdix.model.request.statement.user_tradingstats_request import UserTradingStatsRequest
from rapdix.model.vo.statement.asset_statement_vo import AssetStatementVO
from rapdix.model.vo.statement.user_trading_stats_vo import UserTradingStatsVO
from ..model.page_entity import PageEntity
import json
from typing import Optional, Dict, Any, Tuple, List
from collections import OrderedDict
from rapdix.util.signature_util import SignatureUtil
from rapdix.constants.api_constants import APIConstants
from rapdix.model.response.api_response import ApiResponse
from rapdix.service.base_service import BaseService

class StatementService(BaseService):
    def query_statement(self, request: StatementRequest) -> Optional[ApiResponse[PageEntity[AssetStatementVO]]]:
        """
        Query settlement statement
        
        Args:
            request: Statement query request
        """
        url = f"{self.host}{APIConstants.STATEMENT}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_page_response(response_data, AssetStatementVO)
    
    def query_user_trading_statement(self, request: UserTradingStatsRequest) -> Optional[ApiResponse[UserTradingStatsVO]]:
        """
        Query user trading statement
        
        Args:
            request: User trading stats query request
        """
        url = f"{self.host}{APIConstants.USER_TRADING_STATS}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, UserTradingStatsVO)

