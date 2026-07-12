from fastapi import FastAPI

from app.schema import StockSymbol
from app.utils import get_stock_data
from app.features import create_features
from app.predict import predict_stock

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Stock Prediction API!"
    }


@app.post("/predict")
def predict(stock: StockSymbol):

    try:
        # Download stock data
        data = get_stock_data(stock.symbol)

        # Check if data exists
        if data.empty:
            return {
                "error": f"No data found for symbol '{stock.symbol}'."
            }

        # Generate features
        data = create_features(data)

        # Make prediction
        result = predict_stock(data)

        latest_price = round(float(data["Close"].iloc[-1]), 2)

        return {
            "symbol": stock.symbol,
            "current_price": latest_price,
            "model": "Random Forest",
            **result
        }

    except Exception as e:
        return {
            "error": str(e)
        }