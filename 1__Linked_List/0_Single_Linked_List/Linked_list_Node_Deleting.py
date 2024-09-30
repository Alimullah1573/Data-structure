# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initilise next as null


#*******************************************************************
# Linked List contains a Node object
class LinkedList:
    # Function to initialise head
    def __init__(self):
        self.head = None

    def deletePositionNode(self, position):
        if position == 0:
            self.head = self.head.next

        else:
            node = self.head
            for _ in range(position - 1):
                node = node.next

            node.next = node.next.next

        return self.head

    def printlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next


# *****************************************************************


    def prepend(self, new_data):
        current_node = Node(new_data)

        current_node.next = self.head
        self.head = current_node

#*******************************************************************
if __name__ == '__main__':
    llist = LinkedList()
    llist.prepend(10)
    llist.prepend(20)
    llist.prepend(30)
    llist.prepend(40)

    llist.deletePositionNode(2)
    llist.deletePositionNode(1)

    llist.printlist()

