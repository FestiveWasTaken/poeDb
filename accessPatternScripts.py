from main import *

# AGGREGATION - User can load properties of items that are in their inventory
def get_inventory(user_id):
    collection = get_collection()
    result = collection.aggregate([
        {
            '$match': {
                'inventoryId': user_id
            }
        },
        
        {
            '$project': {
                '_id': 0,
                'id': 1,
                'name': 1,
                'rarity': 1,
                'typeLine': 1,
                'baseType': 1,
                'identified': 1,
                'prefixes': 1,
                'suffixes': 1,
                'note': 1,
                'forum_note': 1,
                'itemDetails': {
                    'w': '$w',
                    'h': '$h',
                    'icon': '$icon',
                    'gridLocation': {
                        'x': '$x',
                        'y': '$y'
                    }
                }
            }
        }
    ])
    
    return result



# AGGREGATION - User can sort items by quality
def sort_by_quality(user_id):
    collection = get_collection()
    result = collection.aggregate([
        {
            '$match': {
                'inventoryId': user_id,
                'quality': { '$exists': True }
            }
        },
        
        {
            '$sort': { 'quality': -1 }
        },
        
        {
            '$project': {
                '_id': 0,
                'id': 1,
                'name': 1,
                'typeLine': 1,
                'baseType': 1,
                'quality': 1,
                'rarity': 1
            }
        }
    ])
    
    return result



# AGGREGATION - Sort users by items in their inventory
def sort_by_inventory_count():
    collection = get_collection()
    result = collection.aggregate([
        {
            '$group': {
                '_id': '$inventoryId',
                'itemCount': { '$sum': 1 }
            },
        },
        
        {
            '$sort': { 'itemCount': -1 }
        },
        
        {
            '$project': {
                '_id': 0,
                'inventoryId': '$_id',
                'itemCount': 1
            }
        }
    ])
    return result



# AGGREGATION - User can search their inventory for items with specific prefixes
def search_by_prefix(user_id, prefix_ids):
    collection = get_collection()
    result = collection.aggregate([
        {
            '$match': {
                'inventoryId': user_id,
                'prefixes': { '$exists': True }
            }
        },
        
        {
            '$unwind': '$prefixes'
        },
        
        {
            '$match': {
                'prefixes': { '$in': prefix_ids }
            }
        },
        
        {
            '$group': {
                '_id': '$prefixes',
                'matchedItems': {
                    '$push': {
                        'id': '$id',
                        'name': '$name',
                        'typeLine': '$typeLine',
                        'baseType': '$baseType'
                    }
                }
            }
        },
        
        {
            '$project': {
                '$_id': 0,
                'prefixId': '$_id',
                'itemCount': { '$size': '$matchedItems' },
                'matchedItems': 1
            }
        }
    ])
    return result



# AGGREGATION - User can group items in their inventory by rarity
def group_by_rarity(user_id):
    collection = get_collection()
    result = collection.aggregate([
        {
            '$match': {
                'inventoryId': user_id
            }
        },
    
        {
            '$group': {
                '_id': '$rarity',
                'count': { '$sum': 1 },
                'items': {
                    '$push': {
                        'id': '$id',
                        'name': '$name',
                        'typeLine': '$typeLine'
                    }
                }
            }
        },
    
        {
            '$project': {
                '$_id': 0,
                'rarity': '$_id',
                'count': 1,
                'sampleItems': { '$slice': ['$items', 5] }
            }
       },
    
        {
            '$sort': { 'count': -1 }
        }
    ])
    return result



# DELETE - Users can drop or delete items 
def delete_item_by_id(item_ids):
    collection = get_collection()
    collection.delete_many({'id': { '$in': item_ids }})
