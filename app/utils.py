import yfinance as yf
import pandas as pd


def get_stock_data(symbol: str) -> pd.DataFrame:
    stock = yf.download(
        symbol,
        period="1y",
        interval="1d"
    )

    # Convert MultiIndex columns to normal columns
    if isinstance(stock.columns, pd.MultiIndex):
        stock.columns = stock.columns.get_level_values(0)

    stock.reset_index(inplace=True)

    return stock