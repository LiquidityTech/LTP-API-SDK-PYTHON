from rapdix.model.request.broker.broker_position_tier_request import BrokerPositionTierRequest
from rapdix.model.request.broker.clearing_statement_request import ClearingStatementRequest
from rapdix.model.request.broker.collection_record_request import CollectionRecordRequest
from rapdix.model.request.broker.fee_rate_request import FeeRateRequest
from rapdix.model.request.broker.sub_portfolio_fee_rate_request import SubPortfolioFeeRateRequest
from rapdix.model.request.broker.subfee_rate_request import SubFeeRateRequest
from rapdix.model.vo.broker.clearing_statement_vo import ClearingStatementVO
from rapdix.model.vo.broker.collection_record_vo import CollectionRecordVO
from rapdix.model.vo.broker.sub_portfolio_fee_rate_vo import SubPortfolioFeeRateVO
from rapdix.model.vo.rules.position_tier_vo import PositionTierVO
from rapdix.model.vo.broker.user_fee_vo import UserFeeVO
from ..model.page_entity import PageEntity
import json
from typing import Optional, Dict, Any, Tuple, List
from collections import OrderedDict
from rapdix.util.signature_util import SignatureUtil
from rapdix.constants.api_constants import APIConstants
from rapdix.model.response.api_response import ApiResponse
from rapdix.service.base_service import BaseService

class BrokerService(BaseService):
    def get_broker_position_tier(self, request: BrokerPositionTierRequest) -> Optional[ApiResponse[Dict[str,List[PositionTierVO]]]]:
        """
        Query broker position tiers
        
        Args:
            request: Broker position tier query request
        """
        url = f"{self.host}{APIConstants.BROKER_POSITION_TIER}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, Dict[str,List[PositionTierVO]])
    
    def set_broker_position_tier(self, request: SubPortfolioFeeRateRequest) -> Optional[ApiResponse[Dict[str,List[SubPortfolioFeeRateVO]]]]:
        """
        Set broker position tiers
        
        Args:
            request: Sub portfolio fee rate request
        """
        url = f"{self.host}{APIConstants.SUB_PORTFOLIO_FEE_RATE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('POST', url, param_map)
        return self._parse_response(response_data, Dict[str,List[SubPortfolioFeeRateVO]])
    
    def get_fee_rate(self, request: FeeRateRequest) -> Optional[ApiResponse[List[UserFeeVO]]]:
        """
        Get fee rate information
        
        Args:
            request: Fee rate query request
        """
        url = f"{self.host}{APIConstants.BROKER_FEE_RATE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, List[UserFeeVO])
    
    def get_sub_portfolio_fee_rate(self, request: SubFeeRateRequest) -> Optional[ApiResponse[List[UserFeeVO]]]:
        """
        Query sub-account fee rates
        
        Args:
            request: Sub fee rate query request
        """
        url = f"{self.host}{APIConstants.BROKER_SUB_FEE_RATE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, List[UserFeeVO])
    
    def get_clearing_statement(self, request: ClearingStatementRequest) -> Optional[ApiResponse[ClearingStatementVO]]:
        """
        Get clearing statement
        
        Args:
            request: Clearing statement query request
        """
        url = f"{self.host}{APIConstants.CLEARING_STATEMENT}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, ClearingStatementVO)
    
    def get_collection_record(self, request: CollectionRecordRequest) -> Optional[ApiResponse[CollectionRecordVO]]:
        """
        Query collection records
        
        Args:
            request: Collection record query request
        """
        url = f"{self.host}{APIConstants.COLLECTION_RECORD}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, CollectionRecordVO)
    
    
