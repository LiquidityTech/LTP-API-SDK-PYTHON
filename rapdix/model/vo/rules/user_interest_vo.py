from dataclasses import dataclass
from typing import Optional

@dataclass
class UserInterestVO:
    level: int
    exchange_type: str
    coin: str
    hour_interest_rate: str
    loan_limit: str
    update_time: Optional[int] = None