from fastapi import FastAPI,HTTPException
from typing import List,Dict

app=FastAPI()

products={
    1:"mango",
    2:"apple",
    3:"banana",
    4:"lemon",
    5:"kiwi"
}

@app.get('/')
def sayhi():
    return("welcome to server")

@app.get('/product/{id}')
def getProduct(id:int):
    return products[id] if products[id] else HTTPException(status_code=404,detail="Product not found")

@app.get("/sort")
def get_sorted(sort_by: str) -> dict[int, str]:
    return dict(
        sorted(
            products.items(),
            reverse=(sort_by != "asc")
        )
    )
