def findOneDocument(collection, query):
    """
    Find a single document matching the query
    """
    try:
        return collection.find_one(query)
    except Exception as e:
        print(f"Error finding document: {e}")
        return None

def findManyDocuments(collection, query, limit=None):
    """
    Find multiple documents matching the query
    """
    try:
        if limit:
            return list(collection.find(query).limit(limit))
        return list(collection.find(query))
    except Exception as e:
        print(f"Error finding documents: {e}")
        return None 