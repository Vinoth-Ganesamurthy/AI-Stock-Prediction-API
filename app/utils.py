import yfinance as yf
import pandas as pd

def get_stock_data(symbol: str):
    stock = yf.download(
        symbol,
        period="1y",
        interval="1d"
    )

    if stock is None:
        raise ValueError("Failed to download stock data.")

    stock.reset_index(inplace=True)

    return stock