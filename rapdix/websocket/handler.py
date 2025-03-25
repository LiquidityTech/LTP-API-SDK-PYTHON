from typing import Optional, Callable
import json

class WebSocketHandler:
    def __init__(self, on_message_callback: Optional[Callable] = None):
        self.on_message_callback = on_message_callback

    def on_message(self, ws, message):
        """Handle received message"""
        print(f"Received message: {message}")
        if self.on_message_callback:
            self.on_message_callback(message)

    def on_error(self, ws, error):
        """Handle error"""
        print(f"Error occurred: {error}")

    def on_close(self, ws):
        """Handle connection close"""
        print("Connection closed")

    def on_open(self, ws):
        """Handle connection open"""
        print("Connection opened") 