def deleteOneDocument(collection, query):
    """
    Delete a single document matching the query
    """
    try:
        result = collection.delete_one(query)
        return result.deleted_count
    except Exception as e:
        print(f"Error deleting document: {e}")
        return None

def deleteManyDocuments(collection, query):
    """
    Delete multiple documents matching the query
    """
    try:
        result = collection.delete_many(query)
        return result.deleted_count
    except Exception as e:
        print(f"Error deleting documents: {e}")
        return None 