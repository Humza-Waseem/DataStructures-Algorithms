# to handle collisions we'll use a technique called linear probing. Here's how it works:

# While inserting a new key-value pair if the target index for a key is occupied by another key, then we try the next index, followed by the next and so on till we the closest empty location.

# While finding a key-value pair, we apply the same strategy, but instead of searching for an empty location, we look for a location which contains a key-value pair with the matching key.

# While updating a key-value pair, we apply the same strategy, but instead of searching for an empty location, we look for a location which contains a key-value pair with the matching key, and update its value.



def getIndex(dataList,a_string):     # func for getting the index for our key(string) ,,, this is an example of Hashing function
    result = 0                       
    for character in a_string: 
        a_number = ord(character)   # we are converting the string(Name) to integer using pythons internal library (ord)
        result+=a_number            #incrementing the integer number we get by converting the string character by character
    ListIndex = result % len(dataList)   # result % the length of list
    return ListIndex


def get_valid_index(dataList, key):
    # Start with the index returned by get_index
    idx = getIndex(dataList,key)
    return idx
    
    # while True:
    #     # Get the key-value pair stored at idx
    #     kv = dataList[idx]
        
    #     # If it is None, return the index
    #     if kv:
    #         return idx
        
    #     # If the stored key matches the given key, return the index
    #     k, v = kv[0],kv[1]
    #     if k == key:
    #         return idx
        
    #     # Move to the next index
    #     idx += 1
        
    #     # Go back to the start if you have reached the end of the array
    #     if idx == len(dataList):
    #         idx = 0



class ProbingHashTable:
    def __init__(self, max_size= 4096):
        # 1. Create a list of size `max_size` with all values None
        self.dataList = [None] * max_size
     
    
    def insert(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.dataList, key)
        
        # 2. Store the key-value pair at the right index
        self.dataList[idx] = (key,value)
    
    
    def find(self, key):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.dataList,key)
        
        # 2. Retrieve the data stored at the index
        kv =  self.dataList[idx]
        
        # 3. Return the value if found, else return None
        return None if kv is None else kv[1]
    
    
    def update(self, key, value):
        # 1. Find the index for the key using get_valid_index
        idx = get_valid_index(self.dataList,key)
        
        # 2. Store the new key-value pair at the right index
        self.dataList[idx] = key,value

    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.dataList if kv is not None]



# Create a new hash table
hash = ProbingHashTable()

# Insert a value
hash.insert('listen', 99)
# hash.insert('silent', 88)


# Check the value
hash.find('listen') 