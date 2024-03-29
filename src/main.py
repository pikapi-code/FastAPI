from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from Models.models import Item

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/ping")
def health_check():
    return {
        "success":True,
        "message": f"successfully reached the API",
        "data": {}
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

   
   