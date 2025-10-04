from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME", "testdb")

client = AsyncIOMotorClient(MONGO_URL)
database = client[DB_NAME]

def get_database():
    return database
