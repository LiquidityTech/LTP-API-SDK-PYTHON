from dataclasses import dataclass
from typing import Optional

@dataclass
class PortfolioDetailRequest:
    """Portfolio detail request"""
    exchangeType: Optional[str] = None
    pageNum: Optional[int] = None
    pageSize: Optional[int] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}