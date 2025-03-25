from dataclasses import dataclass
from typing import Optional

@dataclass
class PositionsCloseRequest:
    """Positions close request"""
    symList: Optional[str] = None
    positionSide: Optional[str] = None
    closeAllPos: Optional[str] = None
    exchangeType: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}