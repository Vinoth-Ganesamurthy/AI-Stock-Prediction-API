from pydantic import BaseModel

class StockData(BaseModel):
    Open: float
    High: float
    Low: float
    Close: float