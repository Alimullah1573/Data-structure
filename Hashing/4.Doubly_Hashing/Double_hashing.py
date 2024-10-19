
"""
Time Complexity (Summary)

Insertion:
1. Best case: O(1)
2. Worst case: O(n) (with multiple collisions)
Search:
1. Best case: O(1)
2. Worst case: O(n) (with multiple collisions)

Deletion:
1. Best case: O(1)
2. Worst case: O(n) (with multiple collisions)

Space Complexity : O(n)
"""




class DoubleHashingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0

    # Primary hash function
    def hash1(self, key):
        return key % self.size

    # Secondary hash function
    def hash2(self, key):
        return 1 + (key % (self.size - 1))

    # Insert a key into the hash table
    def insert(self, key):
        if self.count == self.size:
            print("Hash table is full")
            return

        index = self.hash1(key)
        if self.table[index] is not None:  # Collision detected
            i = 1
            while True:
                new_index = (index + i * self.hash2(key)) % self.size
                if self.table[new_index] is None:
                    self.table[new_index] = key
                    break
                i += 1
        else:
            self.table[index] = key

        self.count += 1

    # Search for a key in the hash table
    def search(self, key):
        index = self.hash1(key)
        i = 0
        while self.table[(index + i * self.hash2(key)) % self.size] is not None:
            if self.table[(index + i * self.hash2(key)) % self.size] == key:
                return (index + i * self.hash2(key)) % self.size                  # return index
            i += 1
        return None

    # Display the hash table
    def display(self):
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")



    def deletion(self,key):
        if self.table is None:
            return None

        index = self.hash1(key)
        i = 0
        while self.table[(index + i * self.hash2(key)) % self.size] is not None:
            if self.table[(index + i * self.hash2(key)) % self.size] == key:
                self.table[(index + i * self.hash2(key)) % self.size] = None
                return True
            i +=1
        return None



# Example usage
hash_table = DoubleHashingHashTable(10)
hash_table.insert(4)
hash_table.insert(6)
hash_table.insert(14)
hash_table.insert(9)
hash_table.insert(12)
hash_table.insert(34)



print("Table : ",hash_table.table)

print("Hash table:")
hash_table.display()

# Searching for an element
print(f"Element 20 found at index: {hash_table.search(34)}")


# before deletion hash_table
print("before deletion hash_table:",hash_table.table)

hash_table.deletion(14) # Deletion

# deletion After hash_table

print("After Deletion list :",hash_table.table)

