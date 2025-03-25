from dataclasses import dataclass
from typing import Optional

@dataclass
class TransactionArchiveVO:
    """Archived transaction record response"""
    transactionId: str
    portfolioId: str
    orderId: str
    exchangeType: str
    businessType: str
    sym: str
    side: str
    quantity: str
    price: str
    tradingFee: str
    tradingFeeCoin: str
    execType: str
    rpnl: str
    createAt: str
    clientOrderId: Optional[str] = None 