# utils/db.py
from pymongo import MongoClient
import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = MongoClient(MONGODB_URI)
db = client["FilamentAI"]

def get_user_collection():
    return db["users"]
