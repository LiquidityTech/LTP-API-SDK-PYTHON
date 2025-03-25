from dataclasses import dataclass

@dataclass
class PositionTierVO:
    sym: str
    min_notional_value: str
    max_notional_value: str
    max_leverage: str
    mm_rate: str
    risk_level: str