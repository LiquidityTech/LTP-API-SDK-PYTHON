from dataclasses import dataclass
from typing import Optional, Dict, Any
import json

@dataclass
class CancelOrdersResponse:
    """WebSocket cancel multiple orders response"""
    id: Optional[str]
    event: str
    code: str
    msg: str

    @classmethod
    def from_dict(cls, data: dict) -> 'CancelOrdersResponse':
        """Create response object from dictionary"""
        return cls(
            id=data.get('id'),
            event=data.get('event', ''),
            code=data.get('code', ''),
            msg=data.get('msg', '')
        ) 