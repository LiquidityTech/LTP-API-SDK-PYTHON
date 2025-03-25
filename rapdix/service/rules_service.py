from rapdix.model.request.rules.discount_rate_request import DiscountRateRequest
from rapdix.model.request.rules.funding_rate_request import FundingRateRequest
from rapdix.model.request.rules.loan_tier_request import LoanTierRequest
from rapdix.model.request.rules.margine_leverage_get_request import MarginLeverageGetRequest
from rapdix.model.request.rules.margine_leverage_set_request import MarginLeverageSetRequest
from rapdix.model.request.rules.mark_price_request import MarkPriceRequest
from rapdix.model.request.rules.position_tier_request import PositionTierRequest
from rapdix.model.request.rules.syminfo_request import SymInfoRequest
from rapdix.model.request.rules.user_interest_request import UserInterestRequest
from rapdix.model.request.rules.user_tradingfee_request import UserTradingFeeRateRequest
from rapdix.model.vo.rules.coin_discount_vo import CoinDiscountVO
from rapdix.model.vo.rules.funding_rate_vo import FundingRateVO
from rapdix.model.vo.rules.loan_tier_vo import LoanTierVO
from rapdix.model.vo.rules.margin_leverage_set_vo import MarginLeverageSetVO
from rapdix.model.vo.rules.margin_leverage_vo import MarginLeverageVO
from rapdix.model.vo.rules.mark_price_vo import MarkPriceVO
from rapdix.model.vo.rules.position_tier_vo import PositionTierVO
from rapdix.model.vo.rules.symbol_info_vo import SymbolInfoVO
from rapdix.model.vo.rules.user_fee_rate_vo import UserFeeRateVO
from rapdix.model.vo.rules.user_interest_vo import UserInterestVO
from ..model.page_entity import PageEntity
import json
from typing import Optional, Dict, Any, Tuple, List
from collections import OrderedDict
from rapdix.util.signature_util import SignatureUtil
from rapdix.constants.api_constants import APIConstants
from rapdix.model.response.api_response import ApiResponse
from rapdix.service.base_service import BaseService

class RulesService(BaseService):
    def set_margin_leverage(self, request: MarginLeverageSetRequest) -> Optional[ApiResponse[MarginLeverageSetVO]]:
        """
        Set margin leverage
        
        Args:
            request: Margin leverage set request
        """
        url = f"{self.host}{APIConstants.MARGIN_LEVERAGE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('POST', url, param_map)
        return self._parse_response(response_data, MarginLeverageSetVO)
    
    def get_margin_leverage(self, request: MarginLeverageGetRequest) -> Optional[ApiResponse[PageEntity[MarginLeverageVO]]]:
        """
        Get margin leverage
        
        Args:
            request: Margin leverage get request
        """
        url = f"{self.host}{APIConstants.MARGIN_LEVERAGE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_page_response(response_data, MarginLeverageVO)
    
    def get_sym_info(self, request: SymInfoRequest) -> Optional[ApiResponse[Dict[str,SymbolInfoVO]]]:
        """
        Query symbol information
        
        Args:
            request: Symbol info query request
        """
        url = f"{self.host}{APIConstants.SYM_INFO}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, Dict[str,SymbolInfoVO])
    
    def get_funding_rate(self, request: FundingRateRequest) -> Optional[ApiResponse[FundingRateVO]]:
        """
        Query current funding rate
        
        Args:
            request: Funding rate query request
        """
        url = f"{self.host}{APIConstants.FUNDING_RATE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, FundingRateVO)
    
    def get_mark_price(self, request: MarkPriceRequest) -> Optional[ApiResponse[MarkPriceVO]]:
        """
        Query mark price
        
        Args:
            request: Mark price query request
        """
        url = f"{self.host}{APIConstants.MARK_PRICE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, MarkPriceVO)
        
    def get_user_fee_rate(self, request: UserTradingFeeRateRequest) -> Optional[ApiResponse[List[UserFeeRateVO]]]:
        """
        Query user fee rate
        
        Args:
            request: User trading fee rate query request
        """
        url = f"{self.host}{APIConstants.USER_FEE_RATE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, List[UserFeeRateVO])
        
    def get_position_tier(self, request: PositionTierRequest) -> Optional[ApiResponse[Dict[str,List[PositionTierVO]]]]:
        """
        Query position tiers
        
        Args:
            request: Position tier query request
        """
        url = f"{self.host}{APIConstants.POSITION_TIER}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, Dict[str,List[PositionTierVO]])
    
    def get_loan_tier(self, request: LoanTierRequest) -> Optional[ApiResponse[List[LoanTierVO]]]:
        """
        Query loan tiers
        
        Args:
            request: Loan tier query request
        """
        url = f"{self.host}{APIConstants.LOAN_TIER}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, List[LoanTierVO])
    
    def get_discount_rate(self, request: DiscountRateRequest) -> Optional[ApiResponse[List[CoinDiscountVO]]]:
        """
        Query discount rate
        
        Args:
            request: Discount rate query request
        """
        url = f"{self.host}{APIConstants.DISCOUNT_RATE}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, List[CoinDiscountVO])
        
    def get_user_interest(self, request: UserInterestRequest) -> Optional[ApiResponse[Dict[str,List[UserInterestVO]]]]:
        """
        Query user interest
        
        Args:
            request: User interest query request
        """
        url = f"{self.host}{APIConstants.USER_INTEREST}"
        param_map = OrderedDict(sorted(request.to_dict().items()))
        response_data = self._make_request('GET', url, param_map)
        return self._parse_response(response_data, Dict[str,List[UserInterestVO]])
        
        