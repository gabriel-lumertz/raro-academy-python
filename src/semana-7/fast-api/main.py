from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def read_root():
    return {'message': 'Hello, FastAPI!'}


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.post('/items/')
async def create_item(item: Item):
    return {'item': item}


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id': item_id}
