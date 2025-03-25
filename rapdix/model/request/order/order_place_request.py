from dataclasses import dataclass
from typing import Optional

@dataclass
class OrderPlaceRequest:
    """Order placement request"""
    sym: str
    side: str
    order_type: str
    order_qty: str
    limit_price: str
    client_order_id: Optional[str] = None
    time_in_force: Optional[str] = None
    quote_order_qty: Optional[str] = None
    reduce_only: Optional[str] = None
    position_side: Optional[str] = None
    tp_trigger_price: Optional[str] = None
    tp_trigger_type: Optional[str] = None
    tp_price: Optional[str] = None
    sl_trigger_price: Optional[str] = None
    sl_trigger_type: Optional[str] = None
    sl_price: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary, only include non-None values and convert to camelCase"""
        name_mapping = {
            'order_type': 'orderType',
            'order_qty': 'orderQty',
            'limit_price': 'limitPrice',
            'client_order_id': 'clientOrderId',
            'time_in_force': 'timeInForce',
            'quote_order_qty': 'quoteOrderQty',
            'reduce_only': 'reduceOnly',
            'position_side': 'positionSide',
            'tp_trigger_price': 'tpTriggerPrice',
            'tp_trigger_type': 'tpTriggerType',
            'tp_price': 'tpPrice',
            'sl_trigger_price': 'slTriggerPrice',
            'sl_trigger_type': 'slTriggerType',
            'sl_price': 'slPrice'
        }
        
        result = {}
        for k, v in self.__dict__.items():
            if v is not None:
                key = name_mapping.get(k, k)  # Use original key if no mapping exists
                result[key] = v
        return result 