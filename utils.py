from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def connectionOpen(connection_string):
    try:
        client = MongoClient(connection_string)
        # Verify connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        return client
    except ConnectionFailure:
        print("Failed to connect to MongoDB. Check your connection string.")
        raise 