from app.utils import get_stock_data
from app.features import create_features

stock = get_stock_data("RELIANCE.NS")
stock = create_features(stock)

print(
    stock[
        [
            "Close",
            "BB_Upper",
            "BB_Lower",
            "BB_Width",
            "Momentum10"
        ]
    ].tail()
)