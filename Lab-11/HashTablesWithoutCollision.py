# # # phone_numbers = {
# # #     'Hamza' : '0320-8425362',
# # #     'Farjad': '0302-4026030',
# # #     'Mama'  : '0323-8878090',
# # #     'Papa'  : '0300-4426324'
# # # }
# # # phone_numbers['Bilal'] = '0324-4355362'
# # # # print(phone_numbers)

# # # print(phone_numbers['Farjad'])



# # # for name in phone_numbers:
# # #     print('Name:', name, ', Phone Number:', phone_numbers[name])



# # maxSizeList = 4096
# # dataList = [None] * maxSizeList
# # print(len(dataList))
# # for i in dataList:
# #     assert i == None


# maxSizeList = 4096
# dataList = [None] * maxSizeList
# print(len(dataList))
# for i in dataList:
#     assert i == None
    
    
# def getIndex(dataList,a_string):     # func for getting the index for our key(string) ,,, this is an example of hashinging function
#     result = 0                       
#     for character in a_string: 
#         a_number = ord(character)   # we are converting the string(Name) to integer using pythons internal library (ord)
#         result+=a_number            #incrementing the integer number we get by converting the string character by character
#     ListIndex = result % len(dataList)   # result % the length of list
#     return ListIndex


# # val  = getIndex(dataList, "Don O Leary") 
# # print(val)

# key, value = 'Hamza', '0320-8425362'  

# idx = getIndex(dataList, key)  # getting the index for storing the above key-value pair

# dataList[idx] = (key, value)   # storing the key-value at the index returned by the dataList

# # data_list[getIndex(data_list, 'Hemanth')] = ('Hemanth', '9595949494')    #getting the index and storing key-value

# #printing the indices
# for items in dataList:
#     if(items != None):
#         key,value = dataList[items]
#         return value
#     else:
#         return 0




# Retrieving items from a hash table
# To retrieve an item from a hash table means to retrieve the value given the key. The way this is done is as follows:
# • Compute the hash value for the key.
# • Find the location in the list corresponding to the hash value.
# • Search the list at that location for the key. In general, there will be a very small number of items in the 
# list (usually one or none), so the search will not take long.
# • If the key is found, return the value. If not, return a "not found" value (this will become clearer later). If 
# there was no list at that location in the array, also return the "not found" value.


def getIndex(dataList,a_string):     # func for getting the index for our key(string) ,,, this is an example of hashinging function
    result = 0                       
    for character in a_string: 
        a_number = ord(character)   # we are converting the string(Name) to integer using pythons internal library (ord)
        result+=a_number            #incrementing the integer number we get by converting the string character by character
    ListIndex = result % len(dataList)   # result % the length of list
    return ListIndex

    # 293 % 4096    ==== 293
    # 400 % 4096    ==== 400
 
class hashingTable:
    
    def __init__(self, max_size=4096):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size

    
    def insert(self, key, value):
        # 1. Find the index for the key using getIndex
        idx = getIndex(self.data_list, key)
        
        # 2. Store the key-value pair at the right index
        self.data_list[idx] = (key,value)
    
    
    def find(self, key):
        # 1. Find the index for the key using getIndex
        idx = getIndex(self.data_list,key)
        
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]
        
        # 3. Return the value if found, else return None
        if kv is None:
            return None
        else:
            key, value = kv
            return value
    
    
    def update(self, key, value):
        # 1. Find the index for the key using getIndex
        idx = getIndex(self.data_list,key)
        
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = (key,value)

    
    def list_all(self):
        # 1. Extract the key from each key-value pair 
        return [kv[0] for kv in self.data_list if kv is not None]


hashing = hashingTable()
hashing.insert("hamza","0320-8425362")
hashing.insert("farjad","0320-8-324262")
hashing.insert("dado","0324-4355360")
hashing.insert("mama","0323-8878090")
hashing.insert("papa","0324-9400204")

hashing.update("papa","0300-4426324")



hashing.update("apap","0302-4426324")     # at papa and apap hashing will be same. i.e the index will be same 
print(hashing.find("papa"))               # so there will be collision


hashing.list_all()

