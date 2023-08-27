
from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool

from src.models import Product, CartItem
from scripts.gen_products import create_mongo

router = APIRouter()
db = create_mongo()


@router.on_event("startup")
async def startup():
    db.products_collection.create_index("id", unique=True)

# @run_in_threadpool
# def blocking_mongo_operation():
#     create_mongo()

# @router.get("/")
# async def read_root():
#     result = await blocking_mongo_operation()
#     return {"result": result}

# @router.get("/generate/", response_model=list[Product])
# def insert_data():
#     from scripts.gen_products import generate
#     if db.count_documents({}) == 0:
#         generate()

@router.get("/products/", response_model=list[Product])
async def get_products():
    try:
        cursor = db.products_db.find({})
        products = [Product(id=str(item["_id"]), **item) for item in cursor]
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/cart/", response_model=CartItem)
def add_to_cart(item: CartItem):
    if item.product_id not in db.products_db:
        raise HTTPException(status_code=400, detail="Product not found")
    
    db.cart_db.append(item.dict())
    return item

@router.get("/cart/", response_model=list[CartItem])
def view_cart():
    return db.cart_db

@router.delete("/cart/{product_id}/")
def remove_from_cart(product_id: int):
    for item in db.cart_db:
        if item['product_id'] == product_id:
            db.cart_db.remove(item)
            return {"status": "Item removed"}
    raise HTTPException(status_code=400, detail="Product not in cart")