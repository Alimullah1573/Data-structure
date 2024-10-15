





class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    # create Hash_function
    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_key = self.hash_function(key)
        self.hash_table[hash_key].append((key, value))

    def search(self, key):
        hash_key = self.hash_function(key)
        bucket = self.hash_table[hash_key]

        for k, val in bucket:
            if k == key:
                return True
        return False

    def get(self, key):
        hash_key = self.hash_function(key)
        bucket = self.hash_table[hash_key]

        # Return all values associated with the key
        values = [val for k, val in bucket if k == key]
        return values if values else None

    def display(self):
        for i, bucket in enumerate(self.hash_table):
            print(f"Bucket {i}: {bucket}")


if __name__ == '__main__':


    # HashTable object creation
    hash_table = HashTable()

    # Insert data
    hash_table.insert(1, "Bangladesh")
    hash_table.insert(2, "India")
    hash_table.insert(3, "Japan")
    hash_table.insert(1, "Canada")
    hash_table.insert(4, "Iceland")
    hash_table.insert(3, "London")


    # hash_Table

    print("full hash_table : ",hash_table.hash_table)

    print()

    # Display hash table
    hash_table.display()



    # Check value presence
    print("\nSearching for key 1:", hash_table.search(1))
    print("Searching for key 3:", hash_table.search(3))

    # Get all values associated with a key
    print("\nValues for key 1:", hash_table.get(1))
    print("Values for key 3:", hash_table.get(3))

    print(hash_table.get(0))
