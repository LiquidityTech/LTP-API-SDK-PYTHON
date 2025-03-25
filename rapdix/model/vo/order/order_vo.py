from dataclasses import dataclass
from typing import Optional

@dataclass
class OrderVO:
    """Order details response"""
    # Required fields
    portfolioId: str
    portfolioName: str
    orderId: str
    orderState: str
    side: str
    exchangeOrderType: str
    exchangeType: str
    businessType: str
    orderQty: str
    orderType: str
    
    # Optional fields
    clientOrderId: str = ""
    sym: str = ""
    quoteOrderQty: Optional[str] = None
    limitPrice: Optional[str] = None
    timeInForce: Optional[str] = None
    executedQty: Optional[str] = None
    executedAmount: Optional[str] = None
    executedAvgPrice: Optional[str] = None
    reason: Optional[str] = None
    createAt: Optional[str] = None
    updateAt: Optional[str] = None
    fee: Optional[str] = None
    feeCoin: Optional[str] = None
    reduceOnly: Optional[bool] = None
    leverage: Optional[int] = None
    lastExecutedQty: Optional[str] = None
    lastExecutedPrice: Optional[str] = None
    lastExecutedAmount: Optional[str] = None
    borrowAmount: Optional[str] = None
    borrowAsset: Optional[str] = None
    positionSide: Optional[str] = None
    algoOrderId: Optional[str] = None
    algoParam: Optional[str] = None
    rebate: Optional[str] = None
    rebateCoin: Optional[str] = None
    tpTriggerPrice: str = ""
    tpTriggerType: str = ""
    tpPrice: str = ""
    slTriggerPrice: str = ""
    slTriggerType: str = ""
    slPrice: str = "" 