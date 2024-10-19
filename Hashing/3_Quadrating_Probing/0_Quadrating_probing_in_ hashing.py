class Hash:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 1

        # Quadratic probing to handle collisions
        while self.hash_table[index] is not None:
            index = (original_index + i ** 2) % self.size
            i += 1

        self.hash_table[index] = key

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        i = 1

        # Search using quadratic probing
        while self.hash_table[index] is not None:
            if self.hash_table[index] == key:
                return index
            index = (original_index + i ** 2) % self.size
            i += 1

        return -1  # Key not found

    def delete(self, key):
        index = self.search(key)
        if index != -1:
            self.hash_table[index] = None
            print(f"Key {key} deleted.")
        else:
            print(f"Key {key} not found.")

    def display(self):
        print("Hash Table:")
        for i, key in enumerate(self.hash_table):
            print(f"Index {i}: {key}")

    def get(self, key):
        index = self.search(key)
        if index != -1:
            return self.hash_table[index]
        else:
            return None

# Example usage
if __name__ == '__main__':
    hash_t = Hash(10)
    hash_t.insert(10)
    hash_t.insert(20)
    hash_t.insert(7)
    hash_t.insert(17)
    hash_t.insert(27)

    # Display the hash table
    hash_t.display()

    # Search for a key
    print("Search for key 20:", hash_t.search(27))

    # Get a key
    print("Get key 27:", hash_t.get(27))

    # Delete a key
    hash_t.delete(17)

    # Display the hash table after deletion
    print(hash_t.hash_table)
