
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


    def sorted_ll(self):
        lis = []
        temp = self.head
        while temp:
            lis.append(temp.data)
            temp = temp.next

        print(sorted(lis))




    def Print_LL(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(10)
    llist.push(50)
    llist.push(33)
    llist.push(-10)

    # Unsorted linked_list
    llist.Print_LL()

    print()

    # sorted_linked_list
    llist.sorted_ll()









