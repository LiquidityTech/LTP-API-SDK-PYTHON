from dataclasses import dataclass
from typing import Optional

@dataclass
class ClearingStatementVO:
    """
    Clearing statement information
    """
    id: Optional[str] = None
    portfolioId: Optional[str] = None
    userId: Optional[str] = None
    exchangeType: Optional[str] = None
    businessType: Optional[str] = None
    transactionId: Optional[str] = None
    statementFlowType: Optional[str] = None
    coin: Optional[str] = None
    amount: Optional[str] = None
    createAt: Optional[str] = None
    updateAt: Optional[str] = None