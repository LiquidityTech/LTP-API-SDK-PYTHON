from dataclasses import dataclass
from typing import Optional

@dataclass
class OrderReplaceRequest:
    """Order replacement request"""
    orderId: str
    replaceQty: str
    replacePrice: str

    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {k: v for k, v in self.__dict__.items()} 