class WebSocketConstants:
    # Private WebSocket URLs
    PRIVATE_WS_URL = "wss://wss.liquiditytech.com/v1/private"
    
    # Public WebSocket URLs
    PUBLIC_WS_URL = "wss://mds.liquiditytech.com/v2/public"
    
    # WebSocket URLs
    REQUEST_PATH = '/users/self/verify'
    METHOD = 'GET'
    
    # Rate Limit
    LOGIN_RATE_LIMIT = 1  # 1 request per second
    
    # Events
    EVENT_LOGIN = "login"
    EVENT_ERROR = "error"
    EVENT_PLACE_ORDER = "place_order"
    EVENT_CANCEL_ORDER = "cancel_order"
    EVENT_CANCEL_ORDERS = "cancel_orders"
    
    # Response Codes
    CODE_SUCCESS = "0"
    CODE_ORDER_SUCCESS = "200000"
    CODE_LOGIN_FAILED = "60009"
    CODE_ORDER_FAILED = "60009"
    
    # Timeouts
    PING_INTERVAL = 28  # seconds, less than 30
    CONNECTION_TIMEOUT = 30  # seconds 
    
    # Order Types
    ORDER_TYPE_LIMIT = "LIMIT"
    ORDER_TYPE_MARKET = "MARKET"
    
    # Order Sides
    ORDER_SIDE_BUY = "BUY"
    ORDER_SIDE_SELL = "SELL"
    
    # Time In Force
    TIME_IN_FORCE_GTC = "GTC"
    TIME_IN_FORCE_IOC = "IOC"
    TIME_IN_FORCE_FOK = "FOK"
    TIME_IN_FORCE_GTX = "GTX"
    
    # Public WebSocket Events
    EVENT_SUBSCRIBE = "SUBSCRIBE"
    EVENT_UNSUBSCRIBE = "UNSUBSCRIBE"
    
    # Channels
    CHANNEL_ORDER_BOOK = "ORDER_BOOK"
    CHANNEL_BBO = "BBO"
    CHANNEL_MARK_PRICE = "MARK_PRICE"
    
    # Trading Side
    SIDE_BUY = "0"
    SIDE_SELL = "1"
    
    # Trading State
    STATE_NORMAL = "0"
    STATE_CLOSE = "1" 