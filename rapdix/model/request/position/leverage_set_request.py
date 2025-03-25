from dataclasses import dataclass
from typing import Optional

@dataclass
class LeverageSetRequest:
    """Leverage setting request"""
    sym: str
    leverage: str

    def to_dict(self) -> dict:
        """Convert to dictionary"""
        return {k: v for k, v in self.__dict__.items()}