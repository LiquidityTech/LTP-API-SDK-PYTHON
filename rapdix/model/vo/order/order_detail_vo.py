from dataclasses import dataclass, field
from typing import Optional

@dataclass
class OrderDetailVO:
    portfolio_id: str
    order_id: str
    client_order_id: str = ""
    order_state: str
    sym: str = ""
    side: str
    order_type: str
    exchange_order_type: str
    exchange_type: str
    business_type: str
    order_qty: str
    quote_order_qty: str
    limit_price: str
    time_in_force: str
    executed_qty: str
    executed_avg_price: str
    executed_amount: str
    reason: str
    create_at: Optional[str] = None
    update_at: Optional[str] = None
    fee: str
    fee_coin: str
    reduce_only: Optional[bool] = None
    leverage: Optional[int] = None
    last_executed_qty: Optional[str] = None
    last_executed_price: Optional[str] = None
    last_executed_amount: Optional[str] = None
    borrow_amount: Optional[str] = None
    borrow_asset: Optional[str] = None
    position_side: Optional[str] = None
    algo_order_id: Optional[str] = None
    algo_param: Optional[str] = None
    rebate: Optional[str] = None
    rebate_coin: Optional[str] = None
    tp_trigger_price: str = field(default="", metadata={"builder_default": True})
    tp_trigger_type: str = field(default="", metadata={"builder_default": True})
    tp_price: str = field(default="", metadata={"builder_default": True})
    sl_trigger_price: str = field(default="", metadata={"builder_default": True})
    sl_trigger_type: str = field(default="", metadata={"builder_default": True})
    sl_price: str = field(default="", metadata={"builder_default": True})