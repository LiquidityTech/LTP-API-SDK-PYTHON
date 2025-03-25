from dataclasses import dataclass
from typing import Optional

@dataclass
class AccountVO:
    """Account information"""
    # Required fields
    portfolioId: str
    exchangeType: str
    equity: str
    maintainMargin: str
    positionValue: str
    accountStatus: str
    marginValue: str
    frozenMargin: str
    perpMargin: str
    debtMargin: str
    openLossMargin: str
    validMargin: str
    availableMargin: str
    upnl: str
    positionMode: str

    # Optional fields
    uniMMR: str = "99999999"
    userId: Optional[str] = None
    perpAvailableMargin: Optional[str] = None
    updateAt: Optional[int] = None 