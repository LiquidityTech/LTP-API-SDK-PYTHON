from dataclasses import dataclass

@dataclass
class PositionsVO:
    sym: str
    order_id: str
    position_side: str
    success: str
    error_msg: str