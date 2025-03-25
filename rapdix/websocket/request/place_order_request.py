from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class PlaceOrderRequest:
    """WebSocket place order request"""
    sym: str
    side: str
    orderType: str
    orderQty: str
    clientOrderId: Optional[str] = None
    timeInForce: Optional[str] = "GTC"
    limitPrice: Optional[str] = None
    quoteOrderQty: Optional[str] = None
    reduceOnly: Optional[str] = None
    positionSide: Optional[str] = None
    tpTriggerPrice: Optional[str] = None
    tpTriggerType: Optional[str] = None
    tpPrice: Optional[str] = None
    slTriggerPrice: Optional[str] = None
    slTriggerType: Optional[str] = None
    slPrice: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format"""
        args = {
            "sym": self.sym,
            "side": self.side,
            "orderType": self.orderType,
            "orderQty": self.orderQty
        }

        # Add optional parameters (if they have values)
        optional_fields = [
            "clientOrderId", "timeInForce", "limitPrice", "quoteOrderQty",
            "reduceOnly", "positionSide", "tpTriggerPrice", "tpTriggerType",
            "tpPrice", "slTriggerPrice", "slTriggerType", "slPrice"
        ]
        
        for field in optional_fields:
            value = getattr(self, field)
            if value is not None:
                args[field] = value

        return {
            "action": "place_order",
            "args": args
        } 