class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        # Linear probing in case of collision
        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size

        return None

    def display(self):
        for i, item in enumerate(self.table):
            if item is not None:
                print(f"Index {i}: Key = {item[0]}, Value = {item[1]}")
            else:
                print(f"Index {i}: Empty")


# Example usage
hash_table = HashTable(10)
hash_table.insert(12, 'Data 1')
hash_table.insert(22, 'Data 2')
hash_table.insert(32, 'Data 3')
hash_table.insert(10,"data 4")
hash_table.insert(20,"data 5")
hash_table.insert(30,"data 6")

# Output: 'Data 2'
print(hash_table.search(22))

# Output data 6
print(hash_table.search(30))


print(hash_table.table)
