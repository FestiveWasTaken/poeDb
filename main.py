from pymongo import MongoClient
from dotenv import load_dotenv
import os
from createScripts import *
from readScripts import *
from updateScripts import *
from deleteScripts import *
from utils import connect_to_mongodb

def main():
    # Load environment variables
    load_dotenv()
    
    # Get MongoDB connection string from environment variable
    connection_string = os.getenv('MONGODB_URI')
    
    # Connect to MongoDB
    client = connect_to_mongodb(connection_string)
    
    # Select database
    db = client['poeDb']
    
    # Your main application logic here
    
if __name__ == "__main__":
    main() 