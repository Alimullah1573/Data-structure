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


    def prepend(self, new_data):
        current_node = Node(new_data)

        current_node.next = self.head
        self.head = current_node




# *****************************************************************


    # get_count : Linked list All data node count
    def get_count(self):
        curretnt_node = self.head
        count = 0
        while curretnt_node:
            curretnt_node = curretnt_node.next
            count +=1
        return count



    def printlist(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next


#*******************************************************************
if __name__ == '__main__':
    llist = LinkedList()
    llist.prepend(10)
    llist.prepend(20)
    llist.prepend(30)
    llist.prepend(40)

    print(llist.get_count())  # Count_list_all Nodes


    llist.printlist()

