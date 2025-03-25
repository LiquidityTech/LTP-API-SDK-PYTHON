from dataclasses import dataclass
from typing import Optional

@dataclass
class MarginLeverageGetRequest:
    """Margin leverage get request"""
    exchangeType: Optional[str] = None
    coin: Optional[str] = None
    page: Optional[str] = None
    pageSize: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}