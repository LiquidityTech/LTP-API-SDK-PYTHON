from dataclasses import dataclass
from typing import Optional

@dataclass
class OrderHistoryRequest:
    """Order history request"""
    sym: Optional[str] = None
    exchange: Optional[str] = None
    businessType: Optional[str] = None
    begin: Optional[str] = None
    end: Optional[str] = None
    page: Optional[str] = None
    pageSize: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary, only include non-None values"""
        return {k: v for k, v in self.__dict__.items() if v is not None} 