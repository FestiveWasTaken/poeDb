from pymongo import MongoClient
from dotenv import load_dotenv
import os
from createScripts import *
from readScripts import *
from updateScripts import *
from deleteScripts import *
from utils import connectionOpen
from createScripts import create_sample_database

def main():
    # Load environment variables
    load_dotenv()
    
    # Get MongoDB connection string from environment variable
    connection_string = os.getenv('MONGODB_URI')
    
    # Connect to MongoDB
    client = connectionOpen(connection_string)
    db = client['poeDb']
    create_sample_database(db['test_items'], 1000)

if __name__ == "__main__":
    main() 

