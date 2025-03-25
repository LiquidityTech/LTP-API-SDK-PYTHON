from dataclasses import dataclass

@dataclass
class OrderReplaceVO:
    """Order replacement response"""
    orderId: str
    orderState: str 