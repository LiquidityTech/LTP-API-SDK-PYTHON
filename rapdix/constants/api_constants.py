class APIConstants:
    # Account
    ACCOUNT = "/api/v1/trading/account"
    
    # Assets
    ASSET_PORTFOLIO_FUNDS_HISTORY = "/api/v1/asset/bills"
    ASSET_PORTFOLIO_DETAIL = "/api/v1/trading/portfolio/assets"
    ASSET_ALL_PORTFOLIO = "/api/v1/user/asset"
    
    # Order
    ORDER = "/api/v1/trading/order"
    ORDERS = "/api/v1/trading/orders"
    ORDER_HISTORY = "/api/v1/trading/history/orders"
    ORDER_HISTORY_ARCHIVE = "/api/v1/trading/archive/history/orders"
    ORDER_CANCEL_ALL = "/api/v1/trading/cancelAll"
    
    # Position
    LEVERAGE_SET = "/api/v1/trading/position/leverage"
    LEVERAGE_GET = "/api/v1/trading/perp/leverage"
    POSITION = "/api/v1/trading/position"
    POSITIONS = "/api/v1/trading/positions"
    POSITIONS_HISTORY = "/api/v1/trading/history/position"
    
    # Transaction
    TRANSACTION = "/api/v1/trading/executions"
    TRANSACTION_PAGEABLE = "/api/v1/trading/executions/pageable"
    TRANSACTION_PAGEABLE_ARCHIVE = "/api/v1/trading/archive/executions/pageable";
    
    # Statement
    STATEMENT = "/api/v1/trading/statement"
    USER_TRADING_STATS = "/api/v1/trading/user/tradingStats"
    
    # Trading Rules
    MARGIN_LEVERAGE = "/api/v1/trading/margin/leverage"
    SYM_INFO = "/api/v1/trading/sym/info"
    FUNDING_RATE = "/api/v1/market/fundingRate"
    MARK_PRICE = "/api/v1/market/markPrice"
    USER_FEE_RATE = "/api/v1/trading/userFeeRate"
    POSITION_TIER = "/api/v1/trading/positionBracket"
    LOAN_TIER = "/api/v1/trading/loan/info"
    DISCOUNT_RATE = "/api/v1/trading/coin/discount"
    USER_INTEREST = "/api/v1/interest/user"
    
    # Broker
    BROKER_POSITION_TIER = "/api/v1/trading/broker/positionBracket"
    SUB_PORTFOLIO_FEE_RATE = "/api/v1/broker/subFeeRate"
    BROKER_FEE_RATE = "/api/v1/broker/feeRate"
    BROKER_SUB_FEE_RATE = "/api/v1/broker/sub/feeRate"
    CLEARING_STATEMENT = "/api/v1/broker/clearingStatement"
    COLLECTION_RECORD = "/api/v1/broker/collectionRecord" 