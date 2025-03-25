import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

from rapdix.config.config import Config
from rapdix.service.order_service import OrderService
from rapdix.model.request.order.order_place_request import OrderPlaceRequest
from rapdix.model.request.order.order_detail_request import OrderDetailRequest
from rapdix.client.rapidx_api_client import RapdixAPIClient
from rapdix.model.request.order.order_history_request import OrderHistoryRequest
from rapdix.model.request.order.current_open_orders_request import CurrentOpenOrdersRequest
from rapdix.model.request.order.order_replace_request import OrderReplaceRequest
from rapdix.model.request.account.account_query_request import AccountQueryRequest

class RapidXDemo:
    def __init__(self):
        self.client = RapdixAPIClient(
            api_key="ABC",
            secret_key="XYZ"
        )

    def run_demo(self):
        request = OrderPlaceRequest(
            sym="BINANCE_PERP_BTC_USDT",
            side="BUY",
            order_type="LIMIT",
            order_qty="1",
            limit_price="3001"
        )
        
        response = self.client.order().place_order(request)
        if response:
            response.print_response("Place Order Result")

        account_request = AccountQueryRequest()
        response = self.client.account().query_account(account_request)
        if response:
            response.print_response("Account Query Result")

        request = OrderDetailRequest(
            order_id="1740401085933000"
        )
        response = self.client.order().query_order(request)
        if response:
            response.print_response("Query Order Result")
    
        history_request = OrderHistoryRequest(
            sym="BINANCE_PERP_BTC_USDT",
            begin="2024-01-01",
            end="2024-01-20",
            page="1",
            pageSize="10"
        )
        response = self.client.order().order_history(history_request)
        if response:
            response.print_response("Order History Result")

        current_open_request = CurrentOpenOrdersRequest(
            sym="BINANCE_PERP_BTC_USDT",
            begin="2024-01-01",
            end="2024-01-20",
            page="1",
            pageSize="10"
        )
        response = self.client.order().current_open_detail(current_open_request)
        if response:
            response.print_response("Current Open Orders Result")

        replace_request = OrderReplaceRequest(
            orderId="1740401085933000",
            replaceQty="2",
            replacePrice="3002"
        )
        response = self.client.order().replace_order(replace_request)
        if response:
            response.print_response("Replace Order Result")


if __name__ == "__main__":
    demo = RapidXDemo()
    demo.run_demo() 