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

    user_pool = ['a2426ff58bb348b2a5f70f8721d31012c8fb892220f641baad4b27520fa0eb67', 'f2c87514c58e42aba36b0483cbee3a1689625e94ad764ee28a04965bcd552c1b', 'aa974fb952a84478b0d6c20c0bddc38c8f46d3cb4fa747e780d9371045aa4302', '180299014a444475a534d784bacea5f9553f04779f8f4ea98508b209dd36a851', 'e30fbfa372034f1598195445c6a5b74859963ac4b1a54009a762e7781ef08ada', '154c456224354ae791922ae8362b8f7893b5936077314b1698c1d61338928b54', '800c0db2bcea4c69b7ef4e2d1bae9eac0d04d8ce26224ab2aea64ea407bb077a', 'ecb06d1958454db59f8a98e68c0defb0085b7f1ecf5845aea2ae11a866421f02', '075d6355756f42349a9c800458dc0fc61e9cba83f30f4079944302cf8fab3c49', 'b825a33043b0429e99f36d3c32f3a94d48bfa8ddac9344d9be14248f924af437', '88e5497a63ee4f4d9a078046a194f1f9f5570e30da3e408ba653ab50d2090ec3', '32318e234b024ad69627fabccc5d53ec91b21d41bd8f49f191da9ace05b2125e', '9855db95201c4ed4a6c8b75aae52a7099d20d7ea83654137a18cb3019b5db127', '31dec8b3f7084c1496dc927c08f8f33be9091785c5a548fbab01f51e60f94185', '7e7c828c7ad9422bb106adf4a78c3e66d62c183b35034fdfb70fc8fc5ae0aaf2', '8b558abd4eec4f2ca4b8250a851173e65d9ddf0daece48cd869442ab0604d20a', '91d2bd4ef3e449f28c2e318704a1364822ad1bee1c6440dd92c937aa681da631', '94679e5398e640138645a6a1b27ce4d41f55f6bb04084ed3896eda3c077f3cc7', 'ab0b4df0ba774a3fb4a53ab12789c09b07cf2176b72846b891f495b3ca44b738', 'faffea23ebe94b4e8351047b3bc94bb04b7ba1decdc84f0fb4b25143d8df2ffd', '3e7e78792c0d4a4a83df47731a2a0a283483df0342024b42b22c41c771407bf2', '9ef128221a23446c89a266e7c813701367a3351087f7470298d7237fa7632a15', '265de197e55e4213b33eccfcccb1f7c2611f36d1e18f4c4b914753a7b5b6cc1a', '0044d51bdb064fd69fab027c734a902a33b53d098d414b22acca0d0d78226400', 'a7089b3b821b43d7846c56c09e8ec17ebaaa71aeb4bb45eeb99407845de57fe8', '528f8e9d9f1b47d08053292aceae8890b17f660ab8c546bdab13b346fbfecd61', '5f6087ff93e94e4b848aba45062149e87727a4143a584ecca3a5aa2b9dbd469a', '053ef135cba841f39c466fb7efb58aabcf783de7c5354ca6813cdf1f2aba1934', '5d681e5498c546a69877726a339affa004a6a396b9774c01a90bb6221c649efd', 'fff20a64c0334b14bcd143666377f3ea62b026bbb67a416eb9ec233f82439359', 'f4300d2f1c9b4014be11f0e327346b7d23d5d6c6d7214f848396af6d00a4e2fd', 'e1c30760a07b49c2854a6c6a9f5184640af54b8d674c446287a4b30c3a76d8df', 'cfe1732dfc8b4780a5b254b2dff1f2adef9c32ad59504ec397950e68a52f88e4', 'e3e16a8926aa42278f4a3d3dc69dcbf97fcad3b969b247679d1bee1d5e56aa8a', '2c363b5fece548bea1e9f54ea38650f803ab010783934a2d992629d64d1807f1', '7f595746e1d04c3da9b0405f4ec7fefd5488824a179d4f27a05938cee576673e', 'fd195393a9cc4d568b7be0a86b01729a50771074e04747129cbc9301c94aeb64', '81da2bde4cb24f4ebb7db3d24547ca56554bbce4f8ed41b2af367dc4a94a9ccc', '801cb342aff74b0283f3aa43df76046bf4a9b88c2c304235932ece80d8e0d7bc', '708ce089b14e46b1a8b8e0186c91b0c2f6a477848e80425f9934490916e30b49', 'a492d9f9937345558e592052dcc9c4f085e0dfc4ba4b48ebb73eff080f76b8bd', '34af7f91f8fd4b259e9842920ddf068cf960e117fd084dfdb39515d71fa8a08a', '00fee8ece96c40c8b58bb27389cabe4ec9afa2b9693f496a9af19f3da7e7ef39', '4be28863f4df4474880f501a853296c100495faf8384445bb3ddbc21e5c13bb0', '348f16a863294f93a24fbe8423e6f4fd5bae8967810e40f9bef9470c87e3efdb', '542d88477a7844039e3d2865530a3a8744832fca1331417296ad5b701e6bdaf3', '49d4de1fcc634b339f8f7f71a230263e850cc932c228428cb1efbb4009a7b700', 'c2b146e653b245e0a9496dc839ac45d15c7cb0ff7013462585b7b918b1029e21', '3e847ae439ce46709fc0569d5636f19f23a5f429efce4602833989736af12c9a', '8f3e2c5eca8c48dda75c6481e28ea37435aa3440cfa94c8d8a80735444916e5b']
    item["inventoryId"] = random.choice(user_pool)  # ?string (unique identifier)
    
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
