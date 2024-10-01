class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Append a node at the end
    def append(self, data):
        new_node = Node(data)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        last = self.head
        while last.next:
            last = last.next

        # Adjust pointers
        last.next = new_node
        new_node.prev = last

    # Prepend a node at the beginning
    def prepend(self, data):
        new_node = Node(data)

        # If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # Adjust pointers
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node


    # Search
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False





    # Print the list forward
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.prepend(5)
dll.prepend(2)

dll.print_list()  # Output: 2 5 10 20
