from dataclasses import dataclass
from typing import Optional
import json

@dataclass
class LoginResponse:
    """WebSocket login response"""
    event: str
    code: str
    msg: str
    id: Optional[str] = None
    data: Optional[dict] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'LoginResponse':
        """Create response object from dictionary"""
        return cls(
            id=data.get('id'),
            event=data.get('event', ''),
            code=str(data.get('code', '')),  
            msg=data.get('msg', ''),
            data=data.get('data')
        )

    def is_success(self) -> bool:
        """Check if login was successful"""
        return self.event == "login" and str(self.code) == "0"

    def __str__(self) -> str:
        """Format output"""
        return json.dumps({
            "id": self.id,
            "event": self.event,
            "code": self.code,
            "msg": self.msg,
            "data": self.data
        }) 