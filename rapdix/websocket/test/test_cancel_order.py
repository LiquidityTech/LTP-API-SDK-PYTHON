import os
import sys
import time
from threading import Thread

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, project_root)

from rapdix.websocket.private_client import PrivateWebSocketClient
from rapdix.config.config import Config
from rapdix.websocket.request.cancel_order_request import CancelOrderRequest

def on_message(message):
    print(f"Custom message handler: {message}")

def main():
    client = PrivateWebSocketClient(
        api_key=Config.API_KEY,
        secret_key=Config.SECRET_KEY,
        on_message_callback=on_message
    )
    
    ws_thread = Thread(target=client.connect)
    ws_thread.daemon = True
    ws_thread.start()
    
    time.sleep(2)
    
    try:
        cancel_request = CancelOrderRequest(
            orderId="your_order_id" 
        )
        
        client.cancel_order(cancel_request)
        
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nDisconnecting...")
        client.disconnect()

if __name__ == "__main__":
    main() 