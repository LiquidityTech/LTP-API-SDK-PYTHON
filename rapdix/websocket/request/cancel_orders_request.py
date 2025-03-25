from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class CancelOrdersRequest:
    """WebSocket cancel multiple orders request"""
    exchangeType: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format"""
        args = {}
        if self.exchangeType:
            args["exchangeType"] = self.exchangeType

        return {
            "action": "cancel_orders",
            "args": args
        } 