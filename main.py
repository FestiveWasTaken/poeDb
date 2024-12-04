from pymongo import MongoClient
from dotenv import load_dotenv
import os
from createScripts import *
from readScripts import *
from updateScripts import *
from deleteScripts import *
from accessPatternScripts import *
from utils import connectionOpen
from createScripts import create_sample_database



def main():
    # Load environment variables
    
    # Get MongoDB connection string from environment variable
    connection_string = "mongodb+srv://joaquincrisologo:Qq1crR4OO047aSQV@testcluster.lq1v5.mongodb.net/?retryWrites=true&w=majority&appName=TestCluster"
    
    # Connect to MongoDB
    client = connectionOpen(connection_string)
    db = client['poeDb']
    collection = db['test_items']
    collection.delete_many({})
    create_sample_database(collection, 1000)

def get_collection():
    connection_string = "mongodb+srv://joaquincrisologo:Qq1crR4OO047aSQV@testcluster.lq1v5.mongodb.net/?retryWrites=true&w=majority&appName=TestCluster"
    client = connectionOpen(connection_string)
    db = client['poeDb']
    collection = db['test_items']
    return collection

if __name__ == "__main__":
    main() 

