from dataclasses import dataclass
from typing import Optional

@dataclass
class PositionPortfolioHistoryRequest:
    """持仓组合历史请求"""
    sym: Optional[str] = None
    exchange: Optional[str] = None
    begin: Optional[str] = None
    end: Optional[str] = None
    page: Optional[str] = None
    pageSize: Optional[str] = None

    def to_dict(self) -> dict:
        """转换为字典，只包含非None值"""
        return {k: v for k, v in self.__dict__.items() if v is not None}