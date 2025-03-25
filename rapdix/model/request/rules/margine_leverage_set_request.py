from dataclasses import dataclass
from typing import Optional

@dataclass
class MarginLeverageSetRequest:
    """Margin leverage request"""
    exchangeType: Optional[str] = None
    leverage: Optional[str] = None
    coin: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}