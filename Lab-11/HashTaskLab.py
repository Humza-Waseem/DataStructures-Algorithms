class KeyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MyHashTable:
    def __init__(self, hsize):
        self.array = [None] * hsize
        self.size = hsize
        self.keys_occupied = 0

    def get_hash_table_size(self):
        return self.size

    def get_number_of_keys(self):
        return self.keys_occupied

    def hash_function(self, key):
        # Simple hash function to calculate index based on the key
        return hash(key) % self.size

    def update_key(self, key, value):
        index = self.hash_function(key)
        if self.array[index] is None:
           
            self.array[index] = KeyNode(key, value)
            self.keys_occupied += 1
        else:
            # Handle collision by linear probing
            while self.array[index] is not None and self.array[index].key != key:
                index = (index + 1) % self.size
            if self.array[index] is None:
                self.array[index] = KeyNode(key, value)
                self.keys_occupied += 1
            else:
                # Key already exists, update the value
                self.array[index].value = value

        # Check if the hash table is full and perform rehash if needed
        if self.keys_occupied >= self.size // 2:
            self.rehash()

    def search_key(self, key):
        index = self.hash_function(key)
        initial_index = index
        while self.array[index] is not None:
            if self.array[index].key == key:
                return self.array[index].value
            index = (index + 1) % self.size
            # Avoid infinite loop in case the key is not present
            if index == initial_index:
                break
        # Key not found
        return None

    def rehash(self):
        # Double the size of the array and reinsert all existing keys
        old_array = self.array
        self.size *= 2
        self.array = [None] * self.size
        self.keys_occupied = 0

        for node in old_array:
            if node is not None:
                self.update_key(node.key, node.value)


# Function to count word occurrences using the MyHashTable
def count_word_occurrences(text):
    words = text.split()
    hash_table = MyHashTable(len(words))
    # print(len(words))
    for word in words:
        count = hash_table.search_key(word)
        if count is not None:
            hash_table.update_key(word, count + 1)
        else:
            hash_table.update_key(word, 1)

    return hash_table


# Example usage:
text = "This is a sample text to demonstrate word counting in a hash table. This text is just a sample."
word_count_table = count_word_occurrences(text)

# Print the word count for each word
for node in word_count_table.array:
    if node is not None:
        print(f"Word: {node.key}, Occurrences: {node.value}")



