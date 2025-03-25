from dataclasses import dataclass
from typing import Dict

@dataclass
class PriceLevel:
    """Price level information"""
    price: str
    qty: str

    @classmethod
    def from_dict(cls, data: Dict) -> 'PriceLevel':
        """Create from dictionary"""
        return cls(
            price=str(data.get('price', '')),
            qty=str(data.get('qty', ''))
        )

@dataclass
class BBO:
    """BBO data model"""
    instId: str
    channel: str
    localTs: str
    exchangeTs: str
    seqNum: str
    exchange: str
    bid: PriceLevel
    ask: PriceLevel

    @classmethod
    def from_dict(cls, data: dict) -> 'BBO':
        """Create from dictionary"""
        return cls(
            instId=data.get('instId', ''),
            channel=data.get('channel', ''),
            localTs=str(data.get('localTs', '')),
            exchangeTs=str(data.get('exchangeTs', '')),
            seqNum=str(data.get('seqNum', '')),
            exchange=data.get('exchange', ''),
            bid=PriceLevel.from_dict(data.get('bid', {})),
            ask=PriceLevel.from_dict(data.get('ask', {}))
        ) 