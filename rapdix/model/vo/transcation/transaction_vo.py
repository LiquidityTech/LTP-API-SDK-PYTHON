from dataclasses import dataclass, field
from typing import Optional

@dataclass
class TransactionVO:
    transaction_id: str
    portfolio_id: str
    order_id: str
    exchange_type: str
    business_type: str
    sym: str
    side: str
    quantity: str = ""
    price: str = ""
    trading_fee: str = ""
    trading_fee_coin: str
    rpnl: str
    client_order_id: str
    algo_order_id: str    
    create_at: str
    exec_type: str
