from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class LoginRequest:
    """WebSocket login request"""
    apiKey: str
    timestamp: str
    sign: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary format"""
        return {
            "action": "login",
            "args": {
                "apiKey": self.apiKey,
                "timestamp": self.timestamp,
                "sign": self.sign
            }
        } 