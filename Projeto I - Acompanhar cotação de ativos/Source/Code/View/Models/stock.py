#Responsavel por montar os modelos no fastapi
from pydantic import BaseModel

class StockFastAPI(BaseModel):
    """ ID, TICKER, PRICE"""
    id:int
    ticker:str
    price:float

class ReitsFastAPI(BaseModel):
    """ ID, TICKER, PRICE"""
    id:int
    ticker:str
    price:float