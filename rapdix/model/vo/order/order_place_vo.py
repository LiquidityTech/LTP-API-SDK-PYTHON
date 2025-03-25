from dataclasses import dataclass
from typing import Optional

@dataclass
class OrderPlaceVO:
    """Order placement response"""
    orderId: str
    clientOrderId: Optional[str] = None 