from app.model import load_model

FEATURES = [
    "Daily_Return",
    "Log_Return",
    "Trading_Range",
    "Price_Change",
    "Volatility20",
    "MA20",
    "MA50",
    "MA200",
    "EMA20"
]


def predict_stock(stock):
    model = load_model()

    latest = stock.iloc[-1]

    X = latest[FEATURES].values.reshape(1, -1)

    prediction = model.predict(X)[0]

    confidence = model.predict_proba(X)[0].max()

    prediction_text = "UP" if prediction == 1 else "DOWN"

    return {
        "prediction": prediction_text,
        "confidence": round(confidence * 100, 2)
    }