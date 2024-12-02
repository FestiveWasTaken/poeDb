def findOneDocument(collection, query):
    try:
        return collection.find_one(query)
    except Exception as e:
        print(f"Error finding document: {e}")
        return None

def findManyDocuments(collection, query, limit=None):
    try:
        if limit:
            return list(collection.find(query).limit(limit))
        return list(collection.find(query))
    except Exception as e:
        print(f"Error finding documents: {e}")
        return None 