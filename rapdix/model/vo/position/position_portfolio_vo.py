from dataclasses import dataclass, field
from typing import Optional

@dataclass
class PositionPortfolioVO:
    position_id: str
    portfolio_id: str
    sym: str = ""
    position_side: str = field(default="NET")
    position_margin: str = ""
    position_mm: str = ""
    position_qty: str = ""
    position_value: str = ""
    unrealized_pnl: str = ""
    unrealized_pnl_rate: str = ""
    avg_price: str = ""
    mark_price: str = ""
    leverage: str = field(default="1")
    max_leverage: str = field(default="20")
    risk_level: str = field(default="1")
    fee: str
    funding_fee: str
    create_at: Optional[str] = None
    update_at: Optional[str] = None
    liq_price: str
    # tpsl_order: Optional[List[AlgoOrderVO]] = None  # Uncomment if needed