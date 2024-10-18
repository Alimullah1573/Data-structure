class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Hash function (simple modulo operation)
    def hash_function(self, key):
        return key % self.size

    # Insert a key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)
        new_node = Node(key, value)

        # If no linked list exists at index, insert node
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            # Collision - append the new node to the linked list
            current = self.table[index]
            while current.next:
                # Update value if the key already exists
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node

    # Search for a key and return its value
    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    # Remove a key-value pair
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next

        return False

    # Display the hash table
    def display(self):
        for i in range(self.size):
            print(f"Index {i}:", end=" ")
            current = self.table[i]
            while current:
                print(f"({current.key}, {current.value})", end=" -> ")
                current = current.next
            print("None")


# Example usage
ht = HashTable(5)

# Insert key-value pairs
ht.insert(10, "Value for 10")
ht.insert(15, "Value for 15")
ht.insert(5, "Value for 5")
ht.insert(22, "Value for 22")

# Display the hash table
ht.display()

# Search for keys
print("Search 10:", ht.search(10))
print("Search 15:", ht.search(15))
print("Search 22:", ht.search(22))

# Delete a key
ht.delete(15)

# Display the hash table after deletion
ht.display()
