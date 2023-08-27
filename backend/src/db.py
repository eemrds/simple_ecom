
# from pymongo import MongoClient

# def create_mongo():
#     client = MongoClient("mongodb://mongo:27017/")  # Update the URI as needed
#     db = client['productDatabase']
#     collection = db['products']
#     if collection.count_documents({}) == 0:
#         from scripts.gen_products import generate
#         generate()

#     return collection