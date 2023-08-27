
import os
import motor.motor_asyncio


def create_mongo():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_CLIENT"))
    db = client["productDatabase"]
    collection = db["products"]
    if collection.count_documents({}) == 0:
        from scripts.gen_products import generate
        generate()

    return collection