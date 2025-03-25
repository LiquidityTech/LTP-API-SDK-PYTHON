import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, parent_dir)

from rapdix.config.config import Config
from rapdix.client.rapidx_api_client import RapdixAPIClient
from rapdix.model.request.transcation.transaction_archive_request import TransactionArchiveRequest

def main():
    client = RapdixAPIClient(
        api_key=Config.API_KEY,
        secret_key=Config.SECRET_KEY
    )

    request = TransactionArchiveRequest(
        sym="BINANCE_PERP_BTC_USDT",
        begin="2024-01-01",
        end="2024-01-20",
        page="1",
        pageSize="10"
    )

    response = client.transaction().query_transaction_archive(request)
    if response:
        response.print_response("Transaction Archive Result")

if __name__ == "__main__":
    main() 