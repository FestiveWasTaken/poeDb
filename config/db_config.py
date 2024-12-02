from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def get_database():
    try:
        # Create a connection using MongoClient
        client = MongoClient(os.getenv('MONGODB_URI'))
        return client  # Return the client instead of the database
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None 