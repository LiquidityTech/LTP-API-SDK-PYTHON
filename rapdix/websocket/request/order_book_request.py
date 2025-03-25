from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class OrderBookSubscription:
    """Order book subscription parameters"""
    channel: str
    instId: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format"""
        return {
            "channel": self.channel,
            "instId": self.instId
        }

@dataclass
class OrderBookRequest:
    """Order book request"""
    subscriptions: List[OrderBookSubscription]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format"""
        return {
            "event": "SUBSCRIBE",
            "arg": [sub.to_dict() for sub in self.subscriptions]
        } 