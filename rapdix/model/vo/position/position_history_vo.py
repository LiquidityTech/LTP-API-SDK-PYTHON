from dataclasses import dataclass, field
from typing import Optional

@dataclass
class PositionHistoryVO:
    position_id: str
    portfolio_id: str
    portfolio_name: str
    sym: str = ""
    closed_type: str
    closed_pnl: str = ""
    closed_pnl_ratio: str = ""
    closed_avg_price: str = ""
    max_position_qty: str = ""
    closed_qty: str = ""
    liq_fee: str = ""
    funding_fee: str = ""
    fee: str = ""
    open_avg_price: str = ""
    leverage: Optional[int] = None
    position_history_side: str
    position_mode: str = field(default="NET")
    create_at: Optional[str] = None
    update_at: Optional[str] = None