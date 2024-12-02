import random
import uuid

def generate_hex_id():
    """Generate a 64-character hexadecimal string"""
    return uuid.uuid4().hex + uuid.uuid4().hex

class ItemSocket:
    def __init__(self, group: int, attr: str):
        self.group = group
        self.attr = attr

def generate_random_item():
    """Generate a random item following the exact data dictionary specifications"""
    
    base_items = {
        "Helmet": {"w": 2, "h": 2, "baseTypes": ["Bascinet", "Burgonet", "Great Helm"]},
        "Body Armour": {"w": 2, "h": 3, "baseTypes": ["Plate Vest", "Chainmail", "Full Plate"]},
    }
    
    item_type = random.choice(list(base_items.keys()))
    base_info = base_items[item_type]
    
    # Required fields
    item = {
        "w": base_info["w"],  # uint
        "h": base_info["h"],  # uint
        "icon": f"path/to/assets/{item_type.lower()}.png",  # string
        "name": "",  # string
        "typeLine": item_type,  # string
        "baseType": random.choice(base_info["baseTypes"]),  # string
        "identified": bool(random.getrandbits(1)),  # bool
        "ilvl": random.randint(1, 100),  # int
    }
    
    # Optional fields (marked with ? in spec)
    if random.random() < 0.5:
        item["socketable"] = bool(random.getrandbits(1))  # ?bool
        
    if random.random() < 0.3:
        item["stackSize"] = random.randint(1, 20)  # ?int
        item["maxStackSize"] = 20  # ?int
        
    if random.random() < 0.4:
        item["league"] = random.choice(["Standard", "Hardcore", "League"])  # ?string
        
    item["id"] = generate_hex_id()  # ?string (64 digit hex)
    
    # Socket-related fields
    if random.random() < 0.3:
        socket_count = random.randint(1, 6)
        item["sockets"] = [  # ?array of ItemSocket
            {
                "group": random.randint(0, 2),
                "attr": random.choice(["S", "D", "I", "G"])
            } for _ in range(socket_count)
        ]
        item["socket"] = socket_count  # ?uint
        item["socketedItems"] = []  # ?array of Item
        
    # Rarity-related fields
    rarities = ["Normal", "Magic", "Rare", "Unique"]
    item["rarity"] = random.choice(rarities)  # ?string
    
    # Optional notes
    if random.random() < 0.2:
        item["note"] = "User note example"  # ?string
        item["forum_note"] = "Forum note example"  # ?string
        
    # Trading locks
    item["lockedToCharacter"] = bool(random.getrandbits(1))  # ?bool
    item["lockedToAccount"] = bool(random.getrandbits(1))  # ?bool
    
    # Description and flavor
    if random.random() < 0.3:
        item["descrText"] = "Item description"  # ?string
        item["flavourText"] = ["Line 1", "Line 2"]  # ?array of string
        
    # Frame and art
    item["frameType"] = random.randint(0, 5)  # ?uint as FrameType
    item["artFilename"] = f"art_{item_type.lower()}"  # ?string
    
    # Affixes
    if random.random() < 0.4:
        item["prefixes"] = [random.randint(1, 100) for _ in range(random.randint(1, 3))]  # ?array of int
        item["suffixes"] = [random.randint(1, 100) for _ in range(random.randint(1, 3))]  # ?array of int
        
    # Grid location
    item["x"] = random.randint(0, 11)  # ?uint
    item["y"] = random.randint(0, 11)  # ?uint
    
    # Quality and inventory
    if random.random() < 0.5:
        item["quality"] = random.randint(0, 100)  # ?int
        
    item["inventoryId"] = generate_hex_id()  # ?string (unique identifier)
    
    if "sockets" in item:
        item["colour"] = random.choice(["S", "D", "I", "G"])  # ?string
        
    return item

def create_sample_database(collection, num_items=10):
    """Create multiple sample items in the database"""
    try:
        items = [generate_random_item() for _ in range(num_items)]
        result = collection.insert_many(items)
        print(f"Successfully created {len(result.inserted_ids)} sample items")
        return result.inserted_ids
    except Exception as e:
        print(f"Error creating sample items: {e}")
        return None 