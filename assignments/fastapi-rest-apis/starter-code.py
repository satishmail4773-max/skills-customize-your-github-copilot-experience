from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student API")


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None


items = [
    {"id": 1, "name": "Laptop", "description": "Work computer", "price": 999.99},
    {"id": 2, "name": "Book", "description": "Python guide", "price": 19.99},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI assignment"}


@app.get("/items")
def get_items():
    return {"items": items}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}


@app.post("/items")
def create_item(item: Item):
    new_item = {"id": len(items) + 1, **item.model_dump()}
    items.append(new_item)
    return new_item
