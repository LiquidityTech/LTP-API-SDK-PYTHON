from dataclasses import dataclass

@dataclass
class LoanTierVO:
    exchange_type: str
    tier: str
    coin: str
    min_size: str
    max_size: str
    mm_rate: str
    max_leverage: str