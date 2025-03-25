from dataclasses import dataclass
from typing import Optional

@dataclass
class PortfolioFundsHistoryRequest:
    """Portfolio funds history request"""
    currency: Optional[str] = None
    type: Optional[int] = None
    status: Optional[int] = None
    startTime: Optional[int] = None  
    endTime: Optional[int] = None   
    page: Optional[int] = None
    pageSize: Optional[int] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}