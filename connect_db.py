import os
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from pathlib import Path
from pymongo import MongoClient
from datetime import datetime


ENV_PATH = Path(__file__).parent / ".env"


def create_connect() -> MongoClient:
    load_dotenv(ENV_PATH)
    client = MongoClient("mongodb://admin:12345@localhost:27017/")

    # client = MongoClient(
    #     os.getenv("MONGO_DB_HOST"),
    #     server_api=ServerApi("1"),
    # )

    return client


if __name__ == "__main__":
    client = create_connect()
    db = client["db-messages"]
    collection = db["messages"]
    cats = collection.find()
    for cat in cats:
        print(cat)
