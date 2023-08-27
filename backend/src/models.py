from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str
    image: str

class CartItem(BaseModel):
    product_id: int
    product_name: str
    quantity: int