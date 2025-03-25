from dataclasses import dataclass, field

@dataclass
class MarkPriceVO:
    public_channel_type_enum: str = field(default="MARK_PRICE")
    sym: str
    mark_price: str
    timestamp: int