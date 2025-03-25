import os
import sys
import time
import json
from threading import Thread

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, project_root)

from rapdix.websocket.public_client import PublicWebSocketClient
from rapdix.websocket.model.order_book import OrderBook
from rapdix.websocket.response.order_book_response import OrderBookResponse

def on_message(message):
    """Custom message processing function"""
    try:
        data = json.loads(message)
        if "arg" in data and data["arg"].get("channel") == "ORDER_BOOK":
            order_book = OrderBook.from_dict(data["data"])
            print(f"Received order book update for {data['arg']['instId']}:")
            print(f"Best bid: {order_book.bids[0] if order_book.bids else 'None'}")
            print(f"Best ask: {order_book.asks[0] if order_book.asks else 'None'}")
    except Exception as e:
        print(f"Error processing message: {e}")
        print(f"Original message: {message}")

def main():
    client = PublicWebSocketClient(on_message_callback=on_message)
    
    ws_thread = Thread(target=client.connect)
    ws_thread.daemon = True
    ws_thread.start()
    
    time.sleep(2)
    
    try:
        inst_ids = [
            "BINANCE_PERP_BTC_USDT",
            "BINANCE_SPOT_BTC_USDT",
            "OKX_SPOT_BTC_USDT",
            "OKX_PERP_BTC_USDT"
        ]
        client.subscribe_order_book(inst_ids)
        
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nUnsubscribing...")
        client.unsubscribe_order_book(inst_ids)
        time.sleep(1)
        print("Disconnecting...")
        client.disconnect()

if __name__ == "__main__":
    main() 