# python program for nth node of inorder traversal
class Node:

    def __init__(self, data):
        self.val = data
        self.left_child = None
        self.right_child = None


index = [0]


# Given binary tree, print the nth node of Preorder tree traversal

def Nth_node_Preorder(root, n):
    if root is None:
        return

    if index[0] <= n:
        if index[0] == n:
            print(root.val)
        index[0] +=1


        Nth_node_Preorder(root.left_child,n)
        Nth_node_Preorder(root.right_child, n)


# Driver Code
if __name__ == '__main__':
    # root node
    root = Node(10)
    """
        1. root = Node(10)

                ____10____
              /            \
            None          None

    """
    root.left_child = Node(20)
    """
        2. root.left_child = Node(20)

                    ____10____
                  /            \
              ___20___        None
    """
    root.right_child = Node(30)
    """
        3. root.right_child = Node(30)

                    ____10____
                  /            \
              ___20___      ___30___
             /        \    /        \
          None       None None      None
    """
    root.left_child.left_child = Node(40)
    """
        4. root.left_child.right_child = Node(40)

                    ____10____
                  /            \
              ___20___      ___30___
             /        \    /        \
           40       None None      None
    """

    # call Nth_node_inorder tree traversal
    # n = int(input())
    n = 2
    Nth_node_Preorder(root, n)


    # it Start From 0  and end n-1
