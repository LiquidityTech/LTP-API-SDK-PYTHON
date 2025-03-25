from dataclasses import dataclass
from typing import Optional, Dict, Any
import json

@dataclass
class PlaceOrderResponse:
    """WebSocket place order response"""
    id: Optional[str]
    event: str
    code: str
    msg: str
    data: Optional[Dict[str, Any]] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'PlaceOrderResponse':
        """Create response object from dictionary"""
        return cls(
            id=data.get('id'),
            event=data.get('event', ''),
            code=data.get('code', ''),
            msg=data.get('msg', ''),
            data=data.get('data')
        )

    def is_success(self) -> bool:
        """Check if order placement was successful"""
        return self.event == "place_order" and self.code == "200000" 