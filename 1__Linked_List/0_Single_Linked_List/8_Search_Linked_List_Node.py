
# Time Complexity  : o(n)
# space Complexity: o(1)


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        current = Node(new_data)
        current.next = self.head
        self.head = current


    def search(self,key):
        if self.head is None:
            return False
        if self.head.data == key:
            return True
        crrent_node = self.head
        while crrent_node.next is not None :
            if crrent_node.next.data == key:
                return True
            crrent_node = crrent_node.next

        else:
            return False

    def Print_LL(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(10)
    llist.push(20)
    llist.push(30)

    # All Linked_list
    llist.Print_LL()
    print()

    # chack linked_list in data


    print(llist.search(10))   # if linked list in data (True) otherwise False
    print(llist.search(40))









