from dataclasses import dataclass

@dataclass
class MarginLeverageVO:
    leverage: str
    exchange_type: str
    coin: str
    sym: str