import json
import ssl
import websocket
import threading
import zlib
from typing import Optional, Callable, List
from .constants import WebSocketConstants
from .handler import WebSocketHandler

class PublicWebSocketClient:
    """Public WebSocket Client"""
    
    def __init__(self, on_message_callback: Optional[Callable] = None):
        """
        Initialize public WebSocket client
        
        Args:
            on_message_callback: Message callback function
        """
        self.handler = WebSocketHandler(on_message_callback)
        self.ws: Optional[websocket.WebSocketApp] = None
        self.is_connected = False

    def _decode_binary_data(self, binary_data):
        """Parse binary data"""
        try:
            decompressed_data = zlib.decompress(binary_data, zlib.MAX_WBITS | 16)
            text_data = decompressed_data.decode('utf-8')
            return text_data
        except Exception as e:
            print(f"Error decoding binary data: {e}")
            return None

    def _on_message(self, ws, message):
        """Handle received message"""
        try:
            if isinstance(message, bytes):
                message = self._decode_binary_data(message)
                if not message:
                    return
            
            self.handler.on_message(ws, message)  # Pass message directly to user's callback function
        except Exception as e:
            print(f"Error in message handler: {e}")

    def _on_open(self, ws):
        """Handle connection open"""
        self.is_connected = True
        self.handler.on_open(ws)

    def _on_close(self, ws):
        """Handle connection close"""
        self.is_connected = False
        self.handler.on_close(ws)

    def connect(self):
        """Establish connection"""
        self.ws = websocket.WebSocketApp(
            WebSocketConstants.PUBLIC_WS_URL,
            on_message=self._on_message,
            on_error=self.handler.on_error,
            on_close=self._on_close,
            on_open=self._on_open
        )
        
        # Start WebSocket
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    def disconnect(self):
        """Close connection"""
        if self.ws:
            self.ws.close()

    def subscribe_order_book(self, inst_ids: List[str]):
        """
        Subscribe to order book data
        
        Args:
            inst_ids: List of instrument IDs
        """
        if self.ws and self.is_connected:
            data = {
                "event": WebSocketConstants.EVENT_SUBSCRIBE,
                "arg": [
                    {
                        "channel": WebSocketConstants.CHANNEL_ORDER_BOOK,
                        "instId": inst_id
                    }
                    for inst_id in inst_ids
                ]
            }
            self.ws.send(json.dumps(data))

    def unsubscribe_order_book(self, inst_ids: List[str]):
        """
        Unsubscribe from order book data
        
        Args:
            inst_ids: List of instrument IDs
        """
        if self.ws and self.is_connected:
            data = {
                "event": WebSocketConstants.EVENT_UNSUBSCRIBE,
                "arg": [
                    {
                        "channel": WebSocketConstants.CHANNEL_ORDER_BOOK,
                        "instId": inst_id
                    }
                    for inst_id in inst_ids
                ]
            }
            self.ws.send(json.dumps(data))

    def subscribe_bbo(self, inst_ids: List[str]):
        """
        Subscribe to BBO data
        
        Args:
            inst_ids: List of instrument IDs
        """
        if self.ws and self.is_connected:
            data = {
                "event": WebSocketConstants.EVENT_SUBSCRIBE,
                "arg": [
                    {
                        "channel": WebSocketConstants.CHANNEL_BBO,
                        "instId": inst_id
                    }
                    for inst_id in inst_ids
                ]
            }
            self.ws.send(json.dumps(data))

    def unsubscribe_bbo(self, inst_ids: List[str]):
        """
        Unsubscribe from BBO data
        
        Args:
            inst_ids: List of instrument IDs
        """
        if self.ws and self.is_connected:
            data = {
                "event": WebSocketConstants.EVENT_UNSUBSCRIBE,
                "arg": [
                    {
                        "channel": WebSocketConstants.CHANNEL_BBO,
                        "instId": inst_id
                    }
                    for inst_id in inst_ids
                ]
            }
            self.ws.send(json.dumps(data))

    def subscribe_mark_price(self, inst_ids: List[str]):
        """
        Subscribe to mark price data
        
        Args:
            inst_ids: List of instrument IDs
        """
        if self.ws and self.is_connected:
            data = {
                "event": WebSocketConstants.EVENT_SUBSCRIBE,
                "arg": [
                    {
                        "channel": WebSocketConstants.CHANNEL_MARK_PRICE,
                        "instId": inst_id
                    }
                    for inst_id in inst_ids
                ]
            }
            self.ws.send(json.dumps(data))

    def unsubscribe_mark_price(self, inst_ids: List[str]):
        """
        Unsubscribe from mark price data
        
        Args:
            inst_ids: List of instrument IDs
        """
        if self.ws and self.is_connected:
            data = {
                "event": WebSocketConstants.EVENT_UNSUBSCRIBE,
                "arg": [
                    {
                        "channel": WebSocketConstants.CHANNEL_MARK_PRICE,
                        "instId": inst_id
                    }
                    for inst_id in inst_ids
                ]
            }
            self.ws.send(json.dumps(data)) 