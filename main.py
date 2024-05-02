from typing import Union
from fastapi import FastAPI
from db.dbInfo import get_tickets

app = FastAPI()


@app.get("/")
def read_root():
    tickets = get_tickets()
    return tickets



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}