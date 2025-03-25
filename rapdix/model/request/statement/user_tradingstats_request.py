from dataclasses import dataclass
from typing import Optional

@dataclass
class UserTradingStatsRequest:
    """User trading stats request"""
    exchange: Optional[str] = None
    businessType: Optional[str] = None
    begin: Optional[str] = None
    end: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}