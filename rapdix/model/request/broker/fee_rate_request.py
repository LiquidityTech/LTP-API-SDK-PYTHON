from dataclasses import dataclass
from typing import Optional

@dataclass
class FeeRateRequest:
    """Fee rate query request"""
    exchange: Optional[str] = None
    instType: Optional[str] = None
    portfolioIds: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary, only include non-None values"""
        return {k: v for k, v in self.__dict__.items() if v is not None}