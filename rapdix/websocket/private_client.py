import json
import hashlib
import hmac
import time
import ssl
import websocket
import threading
from typing import Optional, Callable, List
from .constants import WebSocketConstants
from .handler import WebSocketHandler
from .request.login_request import LoginRequest
from .request.place_order_request import PlaceOrderRequest
from .request.cancel_order_request import CancelOrderRequest
from .request.cancel_orders_request import CancelOrdersRequest
from .response.login_response import LoginResponse

class PrivateWebSocketClient:
    def __init__(self, api_key: str, secret_key: str, on_message_callback: Optional[Callable] = None):
        """
        Initialize WebSocket client
        
        Args:
            api_key: API key
            secret_key: Secret key
            on_message_callback: Message callback function
        """
        self.api_key = api_key
        self.secret_key = secret_key
        self.handler = WebSocketHandler(on_message_callback)
        self.ws: Optional[websocket.WebSocketApp] = None
        self.is_connected = False
        self.ping_thread: Optional[threading.Thread] = None

    def _generate_signature(self) -> tuple[str, str]:
        """Generate signature"""
        timestamp = str(int(time.time()))
        message = timestamp + WebSocketConstants.METHOD + WebSocketConstants.REQUEST_PATH
        
        key = bytes(self.secret_key, 'utf-8')
        data = bytes(message, 'utf-8')
        signature = hmac.new(key, data, hashlib.sha256).hexdigest()
        
        return timestamp, signature

    def _send_login(self, ws):
        """Send login request"""
        timestamp, signature = self._generate_signature()
        login_request = LoginRequest(
            apiKey=self.api_key,
            timestamp=timestamp,
            sign=signature
        )
        ws.send(json.dumps(login_request.to_dict()))

    def _on_message(self, ws, message):
        """Handle received message"""
        try:
            data = json.loads(message)
            if data.get('event') in [WebSocketConstants.EVENT_LOGIN, WebSocketConstants.EVENT_ERROR]:
                self._handle_login_response(message)
            else:
                self.handler.on_message(ws, message)
        except json.JSONDecodeError:
            if message == "pong":
                print("Received pong")
            else:
                print(f"Received non-JSON message: {message}")

    def _start_ping(self, ws):
        """Start sending heartbeat"""
        def ping_thread():
            while self.is_connected:
                time.sleep(28)
                try:
                    ws.send("ping")
                except:
                    break
        
        self.ping_thread = threading.Thread(target=ping_thread)
        self.ping_thread.daemon = True
        self.ping_thread.start()

    def _on_open(self, ws):
        """Handle connection open"""
        self.is_connected = True
        self.handler.on_open(ws)
        self._send_login(ws)  # Private client needs login
        self._start_ping(ws)

    def _on_close(self, ws):
        """Handle connection close"""
        self.is_connected = False
        self.handler.on_close(ws)

    def connect(self):
        """Establish connection"""
        self.ws = websocket.WebSocketApp(
            WebSocketConstants.PRIVATE_WS_URL,  # Use private WebSocket URL
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

    def subscribe_account(self):
        """Subscribe to account information"""
        if self.ws and self.is_connected:
            data = {
                "action": "subscribe",
                "args": {
                    "channel": "account"
                }
            }
            self.ws.send(json.dumps(data))

    def subscribe_position(self):
        """Subscribe to position information"""
        if self.ws and self.is_connected:
            data = {
                "action": "subscribe",
                "args": {
                    "channel": "position"
                }
            }
            self.ws.send(json.dumps(data))

    def subscribe_order(self):
        """Subscribe to order information"""
        if self.ws and self.is_connected:
            data = {
                "action": "subscribe",
                "args": {
                    "channel": "order"
                }
            }
            self.ws.send(json.dumps(data))

    def place_order(self, request: PlaceOrderRequest):
        """
        Place order
        
        Args:
            request: Place order request object
        """
        if self.ws and self.is_connected:
            self.ws.send(json.dumps(request.to_dict()))

    def cancel_order(self, request: CancelOrderRequest):
        """
        Cancel order
        
        Args:
            request: Cancel order request object
        """
        if self.ws and self.is_connected:
            self.ws.send(json.dumps(request.to_dict()))

    def cancel_orders(self, request: CancelOrdersRequest):
        """
        Cancel multiple orders
        
        Args:
            request: Cancel multiple orders request object
        """
        if self.ws and self.is_connected:
            self.ws.send(json.dumps(request.to_dict()))

    def _handle_login_response(self, message: str):
        """Handle login response"""
        try:
            data = json.loads(message)
            response = LoginResponse.from_dict(data)
            print(f"Login response: {response}")  # Just print response, no judgment
            return response
        except Exception as e:
            print(f"Error parsing login response: {e}") 