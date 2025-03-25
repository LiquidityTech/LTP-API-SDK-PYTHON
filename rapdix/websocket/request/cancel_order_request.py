from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class CancelOrderRequest:
    """WebSocket cancel order request"""
    orderId: Optional[str] = None
    clientOrderId: Optional[str] = None

    def __post_init__(self):
        """Validate parameters"""
        if not self.orderId and not self.clientOrderId:
            raise ValueError("Either orderId or clientOrderId must be provided")

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format"""
        args = {}
        if self.orderId:
            args["orderId"] = self.orderId
        if self.clientOrderId:
            args["clientOrderId"] = self.clientOrderId

        return {
            "action": "cancel_order",
            "args": args
        } 