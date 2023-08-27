
import os
import motor.motor_asyncio
from pymongo import MongoClient

async def create_mongo():
    client = client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongo:27017/")  # Update the URI as needed
    db = client['productDatabase']
    collection = db['products']
    if await collection.count_documents({}) == 0:
        from scripts.gen_products import generate
        generate()

    return db