from fastapi import FastAPI
from Models.stock import StockFastAPI, ReitsFastAPI

app = FastAPI()

data = [
    StockFastAPI(id=1, ticker="BBAS3", price=27.30),
    StockFastAPI(id=2, ticker="BBAS4", price=27.30)
]

@app.get("/api/get")
def get_all():
    return data

@app.get("/api/get/{ticket_name}")
def get_specific(ticket_name:str):
    for stock in data:
        if stock.ticker == ticket_name:
            return stock