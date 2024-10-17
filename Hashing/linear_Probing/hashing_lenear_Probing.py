class HashTable:
    def __init__(self, size):
        self.size = size  # Size of the hash table
        self.table = [None] * size  # Initialize table with None

    def hash_function(self, key):
        # Simple hash function using modulo
        return key % self.size

    def insert(self, key):
        hash_index = self.hash_function(key)
        original_index = hash_index
        i = 0  # Linear probing step

        # Try finding an empty slot for the key
        while self.table[hash_index] is not None:
            i += 1
            hash_index = (original_index + i) % self.size  # Linear probing

            if i == self.size:  # Table is full
                raise Exception("Hash table is full")

        # Insert the key at the calculated position
        self.table[hash_index] = key
        print(f"Inserted {key} at index {hash_index}")

    def display(self):
        print("Hash Table: ")
        for i, val in enumerate(self.table):
            print(f"Index {i}: {val}")

# Example Usage
hash_table = HashTable(10)

# Inserting elements
hash_table.insert(10)
hash_table.insert(20)
hash_table.insert(30)
hash_table.insert(40)
hash_table.insert(7)
hash_table.insert(13)

# Display the table
print(hash_table.table)

print()

# Display
hash_table.display()




