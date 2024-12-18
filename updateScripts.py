def updateOneDocument(collection, query, update_data):
    try:
        result = collection.update_one(query, {"$set": update_data})
        return result.modified_count
    except Exception as e:
        print(f"Error updating document: {e}")
        return None

def updateManyDocuments(collection, query, update_data):
    try:
        result = collection.update_many(query, {"$set": update_data})
        return result.modified_count
    except Exception as e:
        print(f"Error updating documents: {e}")
        return None 