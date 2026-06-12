from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float

products: List[Product] = [
    Product(id=1, name="Notebook", description="A ruled notebook for class notes.", price=3.99),
    Product(id=2, name="Pen", description="A blue ink ballpoint pen.", price=1.49),
    Product(id=3, name="Backpack", description="A sturdy backpack for school supplies.", price=29.99),
]

@app.get("/products", response_model=List[Product])
def list_products():
    return products

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products", response_model=Product, status_code=201)
def create_product(product: ProductCreate):
    next_id = max((p.id for p in products), default=0) + 1
    new_product = Product(id=next_id, **product.dict())
    products.append(new_product)
    return new_product
