from dataclasses import dataclass, field
from typing import Optional

@dataclass
class AssetStatementVO:
    user_id: Optional[int] = None
    portfolio_id: int
    request_id: str
    statement_id: str
    coin: str
    sym: str
    statement_type: str
    exchange_type: str
    business_type: str
    before_available: str = ""
    after_available: str = ""
    before_overdraw: str = ""
    after_overdraw: str = ""
    create_at: int