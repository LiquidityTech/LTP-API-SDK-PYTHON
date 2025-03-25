from dataclasses import dataclass
from typing import Optional

@dataclass
class AssetPortfolioHistoryVO:
    """Asset portfolio history"""
    # Optional fields
    id: Optional[str] = None
    currency: Optional[str] = None
    clientOrderId: Optional[str] = None
    amount: Optional[str] = None
    amountReceived: Optional[str] = None
    networkFee: Optional[str] = None
    network: Optional[str] = None
    txld: Optional[str] = None
    fromTradeAccountId: Optional[str] = None
    toTradeAccountId: Optional[str] = None
    fromAccountType: Optional[str] = None
    toAccountType: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    createdAt: Optional[str] = None