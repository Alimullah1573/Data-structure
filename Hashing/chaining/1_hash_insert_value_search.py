class Hash:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # Initialize with empty lists for chaining

    def hash_function(self, key):
        return hash(key) % self.size  # Hash key to an index

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))  # Append key-value pair to the list at the index

    def search(self, key, value):
        index = self.hash_function(key)
        # Check if the key-value pair exists in the chain
        for pair in self.table[index]:
            if pair == (key, value):  # Compare both key and value
                return True
        return False  # Return False if not found

    def display(self):
        for i in range(self.size):
            if self.table[i]:  # If the list at the index is not empty
                print(f"Index {i}: {self.table[i]}")
            else:
                print(f"Index {i}: Empty")

   # spesipic key --->>> value ---- output
    def get_key(self,key):
        index = self.hash_function(key)
        lis = self.table[index]
        for i in lis:
            if i[0] == key:   # chack key
                return i[1] # output value
        return None  # False


if __name__ == '__main__':
    hash_table = Hash(5)  # Create a hash table of size 5
    hash_table.insert(1, 10)
    hash_table.insert(2, 100)
    hash_table.insert(1, 30)

    print("Hash table content:")
    hash_table.display()  # Display the table

    print("\nSearch for (2, 100):", hash_table.search(2, 100))  # Should return True
    print("Search for (1, 40):", hash_table.search(1, 40))  # Should return False

    print(hash_table.search(1,30))
