from config.db_config import get_database

def init_database():
    try:
        # Get MongoDB client
        client = get_database()
        if not client:
            raise Exception("Failed to connect to MongoDB")
            
        # Get/Create database
        db = client['poeDb']
        
        # Create a test collection with one document
        test_collection = db['test_collection']
        test_document = {
            "name": "test",
            "description": "This is a test document"
        }
        
        # Insert the test document
        test_collection.insert_one(test_document)
        
        print("Successfully created database 'poeDb' with test collection!")
        print("Available collections:", db.list_collection_names())
        
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        if client:
            client.close()

if __name__ == "__main__":
    init_database() 