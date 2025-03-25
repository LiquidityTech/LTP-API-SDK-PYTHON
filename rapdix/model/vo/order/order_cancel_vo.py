from dataclasses import dataclass

@dataclass
class OrderCancelVO:
    """Order cancellation response"""
    orderId: str
    orderState: str
    clientOrderId: str = "" 