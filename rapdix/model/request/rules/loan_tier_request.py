from dataclasses import dataclass
from typing import Optional

@dataclass
class LoanTierRequest:
    """Loan tier request"""
    coin: Optional[str] = None
    exchangeType: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}