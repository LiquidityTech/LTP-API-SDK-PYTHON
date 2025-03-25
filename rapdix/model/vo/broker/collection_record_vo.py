from dataclasses import dataclass
from typing import Optional

@dataclass
class CollectionRecordVO:
    user_id: Optional[str] = None
    portfolio_id: Optional[str] = None
    sub_portfolio_id: Optional[str] = None
    exchange_type: Optional[str] = None
    business_type: Optional[str] = None
    transaction_id: Optional[str] = None
    coin: Optional[str] = None
    amount: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None