import os
import sys
import time
import json
from threading import Thread

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, project_root)

from rapdix.websocket.public_client import PublicWebSocketClient
from rapdix.websocket.model.mark_price import MarkPrice
from rapdix.websocket.response.mark_price_response import MarkPriceResponse

def on_message(message):
    try:
        data = json.loads(message)
        if "channel" in data and data["channel"] == "MARK_PRICE":
            mark_price = MarkPrice.from_dict(data)
            print(f"\nReceived Mark Price update for {mark_price.instId}:")
            print(f"Mark Price: {mark_price.markPrice}")
            print(f"Local Time: {mark_price.localTs}")
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
        inst_ids = ["OKX_PERP_BTC_USDT"]
        client.subscribe_mark_price(inst_ids)
        
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nUnsubscribing...")
        client.unsubscribe_mark_price(inst_ids)
        time.sleep(1)
        print("Disconnecting...")
        client.disconnect()

if __name__ == "__main__":
    main() 