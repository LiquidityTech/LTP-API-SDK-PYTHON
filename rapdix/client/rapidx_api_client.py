from typing import Optional
from rapdix.service.order_service import OrderService
from rapdix.service.account_service import AccountService
from rapdix.service.asset_service import AssetService

class RapdixAPIClient:
    def __init__(self, api_key: str, secret_key: str, base_url: str = "https://api.liquiditytech.com"):
        """
        RapidX API client
        
        Args:
            api_key: API key
            secret_key: secret key
            base_url: API base url
        """
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url
        
        self._order_service: Optional[OrderService] = None
        self._account_service: Optional[AccountService] = None
        self._asset_service: Optional[AssetService] = None
  

    def order(self) -> OrderService:
        """Get order service"""
        if self._order_service is None:
            self._order_service = OrderService(
                host=self.base_url,
                api_key=self.api_key,
                secret_key=self.secret_key
            )
        return self._order_service

    def account(self) -> AccountService:
        """Get account service"""
        if self._account_service is None:
            self._account_service = AccountService(
                host=self.base_url,
                api_key=self.api_key,
                secret_key=self.secret_key
            )
        return self._account_service

    def asset(self) -> AssetService:
        """Get asset service"""
        if self._asset_service is None:
            self._asset_service = AssetService(
                host=self.base_url,
                api_key=self.api_key,
                secret_key=self.secret_key
            )
        return self._asset_service
