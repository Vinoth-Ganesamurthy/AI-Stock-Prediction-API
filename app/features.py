import pandas as pd
import numpy as np


def create_features(stock):
    stock = stock.copy()

    stock["Daily_Return"] = stock["Close"].pct_change()

    stock["Log_Return"] = np.log(
        stock["Close"] / stock["Close"].shift(1)
    )

    stock["Trading_Range"] = stock["High"] - stock["Low"]

    stock["Price_Change"] = stock["Close"] - stock["Open"]

    stock["Volatility20"] = (
        stock["Daily_Return"]
        .rolling(window=20)
        .std()
    )

    stock["MA20"] = stock["Close"].rolling(20).mean()
    stock["MA50"] = stock["Close"].rolling(50).mean()
    stock["MA200"] = stock["Close"].rolling(200).mean()

    stock["EMA20"] = (
        stock["Close"]
        .ewm(span=20, adjust=False)
        .mean()
    )

    return stock