from dataclasses import dataclass

@dataclass
class UserFeeRateVO:
    exchange_type: str
    business_type: str
    taker_fee_rate: str
    maker_fee_rate: str
    level: str