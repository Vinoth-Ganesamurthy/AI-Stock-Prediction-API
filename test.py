from app.utils import get_stock_data
from app.features import create_features

stock = get_stock_data("RELIANCE.NS")

stock = create_features(stock)

print(stock[[
    "Close",
    "Daily_Return",
    "Log_Return",
    "Trading_Range",
    "Price_Change",
    "MA20",
    "MA50",
    "EMA20"
]].tail())