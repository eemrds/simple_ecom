
import os
import random
from PIL import Image, ImageDraw, ImageFont
import motor.motor_asyncio
from pymongo import MongoClient


PRODUCT = [
    {
        "name": "OnePlus One",
        "price": 299.00,
        "description": "OnePlus's first product, known as the '2014 Flagship Killer.'",
        "image": "https://www.oneplus.com/one"
    },
    {
        "name": "OnePlus 2",
        "price": 349,  # Price varies
        "description": "Successor to the OnePlus One, promoted as the '2016 Flagship killer.'",
        "image": "https://www.oneplus.com/2"
    },
    {
        "name": "OnePlus 3",
        "price": 399,  # Price varies
        "description": "First OnePlus device not part of the invite system, featuring a Qualcomm Snapdragon 820 and 6 GB of RAM.",
        "image": "https://www.oneplus.com/3"
    },
    {
        "name": "OnePlus 5",
        "price": 599,  # Price varies
        "description": "Launched with a Qualcomm Snapdragon 835, a dual-lens camera setup, up to 8 GB RAM, and up to 128 GB of storage.",
        "image": "https://www.oneplus.com/5"
    },
    {
        "name": "OnePlus 5T",
        "price": 549,  # Price varies
        "description": "Successor to the OnePlus 5, featuring the same Qualcomm Snapdragon 835 SoC and storage options as its predecessor.",
        "image": "https://www.oneplus.com/5t"
    }
]

async def create_mongo():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongo:27017/")
    db = client["productDatabase"]
    collection = db["products"]
    if await collection.count_documents({}) == 0:
        generate()

    return db


def generate():
    db = create_mongo()
    for item in PRODUCT:
        db.products.insert_one(item)
