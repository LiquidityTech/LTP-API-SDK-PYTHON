from dataclasses import dataclass
from typing import Optional

@dataclass
class UserFeeVo:
    portfolio_id: Optional[str] = None
    exchange: Optional[str] = None
    inst_type: Optional[str] = None
    eff_date: Optional[str] = None
    maker: Optional[str] = None
    taker: Optional[str] = None