from dataclasses import dataclass
from typing import Optional

@dataclass
class TransactionRequest:
    """Transaction request"""
    orderId: Optional[str] = None
    sym: Optional[str] = None
    begin: Optional[str] = None
    end: Optional[str] = None
    limit: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}