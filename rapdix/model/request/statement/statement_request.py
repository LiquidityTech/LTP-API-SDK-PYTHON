from dataclasses import dataclass
from typing import Optional

@dataclass
class StatementRequest:
    """Statement request"""
    coin: Optional[str] = None
    sym: Optional[str] = None
    statementType: Optional[str] = None
    exchange: Optional[str] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    page: Optional[str] = None
    pageSize: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary, only include non-None values"""
        return {k: v for k, v in self.__dict__.items() if v is not None}