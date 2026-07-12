import pandas as pd
import numpy as np


def create_features(stock):
    stock = stock.copy()

    # Daily Return
    stock["Daily_Return"] = stock["Close"].pct_change()

    # Log Return
    stock["Log_Return"] = np.log(
        stock["Close"] / stock["Close"].shift(1)
    )

    # Trading Range
    stock["Trading_Range"] = stock["High"] - stock["Low"]

    # Price Change
    stock["Price_Change"] = stock["Close"] - stock["Open"]

    # Volatility
    stock["Volatility20"] = (
        stock["Daily_Return"]
        .rolling(window=20)
        .std()
    )

    # Moving Averages
    stock["MA20"] = stock["Close"].rolling(20).mean()
    stock["MA50"] = stock["Close"].rolling(50).mean()
    stock["MA200"] = stock["Close"].rolling(200).mean()

    # Exponential Moving Average
    stock["EMA20"] = (
        stock["Close"]
        .ewm(span=20, adjust=False)
        .mean()
    )

    # RSI
    delta = stock["Close"].diff()

    gain = delta.where(delta > 0, 0)

    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()

    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss

    stock["RSI"] = 100 - (100 / (1 + rs))

    # MACD
    ema12 = stock["Close"].ewm(span=12, adjust=False).mean()

    ema26 = stock["Close"].ewm(span=26, adjust=False).mean()

    stock["MACD"] = ema12 - ema26

    stock["MACD_Signal"] = (
        stock["MACD"]
        .ewm(span=9, adjust=False)
        .mean()
    )

    # Bollinger Bands
    rolling_std = stock["Close"].rolling(20).std()

    stock["BB_Upper"] = stock["MA20"] + (2 * rolling_std)

    stock["BB_Lower"] = stock["MA20"] - (2 * rolling_std)

    stock["BB_Width"] = (
        stock["BB_Upper"] - stock["BB_Lower"]
    )

    # Momentum (10-day)
    stock["Momentum10"] = (
        stock["Close"] - stock["Close"].shift(10)
    )

    return stock