from dataclasses import dataclass
from typing import Optional

@dataclass
class SymbolInfoVO:
    sym: str
    original_symbol: str
    state: str
    price_precision: str
    qty_precision: str
    lot_size: str
    tick_size: str
    min_notional: str
    max_limit_size: str
    max_market_size: str
    max_num_orders: str
    min_size: Optional[str] = None
    contract_size: Optional[str] = None
    default_leverage: Optional[str] = None
    min_limit_size: Optional[str] = None
    min_market_quote_size: Optional[str] = None
    max_market_quote_size: Optional[str] = None
    min_market_base_size: Optional[str] = None
    max_market_base_size: Optional[str] = None