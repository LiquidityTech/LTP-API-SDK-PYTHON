from dataclasses import dataclass
from typing import Optional

@dataclass
class BrokerPositionTierRequest:
    """Broker position tier request"""
    sym: Optional[str] = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}