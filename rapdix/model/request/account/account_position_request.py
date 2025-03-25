from dataclasses import dataclass
from typing import Optional

@dataclass
class AccountPositionModeRequest:
    """Account position mode request"""
    exchangeType: Optional[str] = None
    positionMode: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}