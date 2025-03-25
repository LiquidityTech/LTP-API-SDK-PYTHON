from dataclasses import dataclass
from typing import Optional

@dataclass
class SubPortfolioFeeRateRequest:
    """Sub portfolio fee rate request"""
    portfolioId: Optional[str] = None
    exchange: Optional[str] = None
    instType: Optional[str] = None
    chgType: Optional[str] = None
    chgTaker: Optional[str] = None
    chgMaker: Optional[str] = None
    effDate: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}