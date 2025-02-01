from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

# Create a MongoClient using the URI from the environment
client = MongoClient(MONGODB_URI)

# Access the 'DemoApp' database
db = client["DemoApp"]

# Function to get the 'users' collection
def get_user_collection():
    return db["users"]
