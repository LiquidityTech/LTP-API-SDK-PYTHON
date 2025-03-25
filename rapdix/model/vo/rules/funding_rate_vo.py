from dataclasses import dataclass

@dataclass
class FundingRateVO:
    funding_rate: str
    funding_time: str
    sym: str
    next_funding_time: str