from dataclasses import dataclass
from typing import Optional

@dataclass
class AssetVO:
    """Asset information"""
    # Required fields
    portfolioId: str
    coin: str
    total: str
    available: str
    frozen: str
    btcValue: str
    usdtValue: str
    exchangeType: str
    balance: str

    # Optional fields
    debt: str = ""
    equity: str = ""
    borrowAmount: Optional[str] = None
    interest: Optional[str] = None
    interestRate: Optional[str] = None
    marginRatio: Optional[str] = None
    unrealizedProfit: Optional[str] = None
    marginFrozen: Optional[str] = None
    borrowInterest: Optional[str] = None
    updateTime: Optional[int] = None
    userId: Optional[str] = None
    createAt: Optional[str] = None
    updateAt: Optional[str] = None
    overdraw: Optional[str] = None
    indexPrice: Optional[str] = None
    marginValue: Optional[str] = None
    virtualBorrow: Optional[str] = None
    upnl: Optional[str] = None
    debtMargin: Optional[str] = None
    perpMargin: Optional[str] = None
    maxTransferable: Optional[str] = None
    equityValue: Optional[str] = None