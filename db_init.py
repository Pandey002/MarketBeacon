import os

from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

def initialize_database():
    mongo_uri = os.getenv("MONGO_URI")
    mongo_db = os.getenv("MONGO_DB")

    if not mongo_uri or not mongo_db:
        raise ValueError("MONGO_URI or MONGO_DB is not set in the environment variables.")

    client = MongoClient(mongo_uri)
    db = client[mongo_db]

    # Example collection for storing scraped data
    if "scraped_data" not in db.list_collection_names():
        db.create_collection("scraped_data", capped=False)
    print("MongoDB initialized successfully.")

if __name__ == "__main__":
    initialize_database()