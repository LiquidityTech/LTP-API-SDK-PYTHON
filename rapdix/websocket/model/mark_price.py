from dataclasses import dataclass

@dataclass
class MarkPrice:
    """Mark price data model"""
    channel: str
    localTs: str
    instId: str
    markPrice: str

    @classmethod
    def from_dict(cls, data: dict) -> 'MarkPrice':
        """Create from dictionary"""
        return cls(
            channel=data.get('channel', ''),
            localTs=str(data.get('localTs', '')),
            instId=data.get('instId', ''),
            markPrice=str(data.get('markPrice', ''))
        ) 