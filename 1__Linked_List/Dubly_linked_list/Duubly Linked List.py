class Node:
    def __init__(self,data = None,prev = None,next = None):
        self.data = data
        self.prev = prev
        self.next = next
    def __repr__(self):
        return repr(self.data)


class linked_list:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []
        current_node = self.head.next
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next

        return ','.join(nodes)

    def append(self,data):
        node = Node(data)
        if self.head.next is None:
            self.head.next = node
            return
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next
        current_node.next = node
        node.prev = current_node


    def Prepend(self,data):
        frist_node = self.head.next
        new_node = Node(data,None,frist_node)
        self.head.next = new_node
        if frist_node:
            frist_node.prev = new_node
q = linked_list()
q.Prepend(90)

q.append(4)
print(q)