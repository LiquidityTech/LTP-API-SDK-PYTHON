from dataclasses import dataclass
from typing import Optional

@dataclass
class LeverageGetRequest:
    """Leverage query request"""
    sym: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary, only include non-None values"""
        return {k: v for k, v in self.__dict__.items() if v is not None}