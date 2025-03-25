from dataclasses import dataclass, field
from typing import List, Optional

from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class UserTradingStatsDTO:
    exchange: str
    business_type: str
    executed_amount: str

@dataclass
class UserTradingStatsVO:
    user_id: Optional[str] = None
    begin: str
    end: str
    all_spot: str
    all_perp: str
    details: List[UserTradingStatsDTO] = field(default_factory=list)