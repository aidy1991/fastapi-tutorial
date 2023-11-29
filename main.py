from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel
import openapi_client

app = FastAPI()


api_client = openapi_client.ApiClient()
api_instance = openapi_client.DefaultApi(api_client)
api_response = api_instance.read_item_items_item_id_get()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


class ItemResponse(BaseModel):
    item_id: int
    q: str | None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int, q: str | None = None) -> Any:
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}
