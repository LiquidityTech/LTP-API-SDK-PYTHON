from dataclasses import dataclass

@dataclass
class MarkPriceResponse:
    """Mark price data response"""
    channel: str
    localTs: str
    instId: str
    markPrice: str

    @classmethod
    def from_dict(cls, data: dict) -> 'MarkPriceResponse':
        """Create from dictionary"""
        return cls(
            channel=data.get('channel', ''),
            localTs=str(data.get('localTs', '')),
            instId=data.get('instId', ''),
            markPrice=str(data.get('markPrice', ''))
        ) 