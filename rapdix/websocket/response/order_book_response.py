from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass
class Trade:
    """Trade information"""
    price: str
    quantity: str
    side: str
    exchange_ts: str

    @classmethod
    def from_list(cls, data: List) -> 'Trade':
        """Create from list"""
        return cls(
            price=data[0],
            quantity=data[1],
            side=data[2],
            exchange_ts=data[3]
        )

@dataclass
class OrderBookResponse:
    """Order book data response"""
    local_ts: str
    exchange_ts: str
    seq_num: str
    type: str
    pre_seq_num: str
    ltp: str
    ttv: str
    ttq: str
    state: str
    bids: List[Tuple[str, str]]
    asks: List[Tuple[str, str]]
    trades: List[Trade]

    @classmethod
    def from_dict(cls, data: dict) -> 'OrderBookResponse':
        """Create from dictionary"""
        return cls(
            local_ts=str(data.get('localTs', '')),
            exchange_ts=str(data.get('exchangeTs', '')),
            seq_num=str(data.get('seqNum', '')),
            type=data.get('type', ''),
            pre_seq_num=str(data.get('preseqNum', '')),
            ltp=data.get('ltp', ''),
            ttv=data.get('ttv', ''),
            ttq=data.get('ttq', ''),
            state=data.get('state', ''),
            bids=[(str(bid[0]), str(bid[1])) for bid in data.get('bids', [])],
            asks=[(str(ask[0]), str(ask[1])) for ask in data.get('asks', [])],
            trades=[Trade.from_list(trade) for trade in data.get('trades', [])]
        ) 