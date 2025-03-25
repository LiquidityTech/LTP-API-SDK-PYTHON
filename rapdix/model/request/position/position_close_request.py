from dataclasses import dataclass
from typing import Optional

@dataclass
class PositionCloseRequest:
    """Position close request"""
    sym: str
    positionSide: str

    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {k: v for k, v in self.__dict__.items()}