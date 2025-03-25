import os
import sys
import time
import json
from threading import Thread

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, project_root)

from rapdix.websocket.public_client import PublicWebSocketClient
from rapdix.websocket.model.bbo import BBO
from rapdix.websocket.response.bbo_response import BboResponse

def on_message(message):
    try:
        data = json.loads(message)
        if "channel" in data and data["channel"] == "BBO":
            bbo = BBO.from_dict(data)
            print(f"\nReceived BBO update for {bbo.instId}:")
            print(f"Bid: {bbo.bid.price} @ {bbo.bid.qty}")
            print(f"Ask: {bbo.ask.price} @ {bbo.ask.qty}")
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
        inst_ids = ["BINANCE_PERP_BTC_USDT"]
        client.subscribe_bbo(inst_ids)
        
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nUnsubscribing...")
        client.unsubscribe_bbo(inst_ids)
        time.sleep(1)
        print("Disconnecting...")
        client.disconnect()

if __name__ == "__main__":
    main() 