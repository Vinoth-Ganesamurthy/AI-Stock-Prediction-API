from fastapi import FastAPI
from app.schema import StockData

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Stock Prediction API!"
    }

@app.post("/predict")
def predict(stock: StockData):
    return {
        "message": "Data received successfully!",
        "received_data": stock
    }