def insert_one_document(collection, document):
    """
    Insert a single document into the specified collection
    """
    try:
        result = collection.insert_one(document)
        return result.inserted_id
    except Exception as e:
        print(f"Error inserting document: {e}")
        return None

def insert_many_documents(collection, documents):
    """
    Insert multiple documents into the specified collection
    """
    try:
        result = collection.insert_many(documents)
        return result.inserted_ids
    except Exception as e:
        print(f"Error inserting documents: {e}")
        return None 