from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()




class Item(BaseModel):
    name: str
    description: Optional[str]=None
    price: float
    tax: Optional[float]=None
    

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
        

@app.get("/justtest")
def just_test():
    return {"item": "tested"}

@app.post("/items/")
async def create_item(item: Item):
    return item
