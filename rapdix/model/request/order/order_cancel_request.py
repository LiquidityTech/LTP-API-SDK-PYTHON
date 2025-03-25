from dataclasses import dataclass
from typing import Optional

@dataclass
class OrderCancelRequest:
    """Order cancellation request"""
    order_id: Optional[str] = None
    client_order_id: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary, only include non-None values and convert to camelCase"""
        name_mapping = {
            'order_id': 'orderId',
            'client_order_id': 'clientOrderId'
        }
        
        result = {}
        for k, v in self.__dict__.items():
            if v is not None:
                key = name_mapping.get(k, k)
                result[key] = v
        return result 