

class Node:

    def __init__(self, data):
        self.val = data
        self.left_child = None
        self.right_child = None


def Inorder_Tree_Traversal(root):
    if root:
        Inorder_Tree_Traversal(root.left_child)
        print(root.val, end=" ")
        Inorder_Tree_Traversal(root.right_child)


def insert_Node(root, key):
    if root is None:
        return Node(key)

    else:
        if root.val == key:
            return root

        elif root.val < key:
            root.right_child = insert_Node(root.right_child, key)

        else:
            root.left_child = insert_Node(root.left_child, key)

    return root



if __name__ == '__main__':
    """
    Before Binary Tree:

                     ____50____
                   /            \
               ___20___      ___60___
              /        \    /        \
            10         25  45        70
           /  \
          1  None

    """
    root = Node(50)

    root.left_child = Node(20)
    root.right_child = Node(60)

    root.left_child.left_child = Node(10)
    root.left_child.right_child = Node(25)

    root.right_child.left_child = Node(45)
    root.right_child.right_child = Node(70)

    root.left_child.left_child.left_child = Node(1)

    # call inorder function
    print("Print Binary Tree Inorder Traversal:")
    Inorder_Tree_Traversal(root)

    """
    After Binary Tree:

                         ____50____
                       /            \
                   ___20___      ___60___
                  /        \    /        \
                10         25  50        70
               /  \            /
              1  None         45

    """

    # call insert_Node function
    insert_Node(root, 9)

    print("\n\nPrint Binary Tree Inorder Traversal:")
    Inorder_Tree_Traversal(root)



#---------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>





class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
class Tree:
    def createNode(self,data):
      return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data<node.data :
            node.left = self.insert(node.left,data)

        else:
            node.right = self.insert(node.right,data)
        return node

    # Tree inorder
    def tree_INorder(self,root):
        if root is not None:
            self.tree_INorder(root.left)
            print(root.data,end=' ')
            self.tree_INorder(root.right)

    # Tree Pre_order
    def Pre_order(self,root):
        if root is not  None:
            print(root.data,end=' ')
            self.Pre_order(root.left)
            self.Pre_order(root.right)


    # Tree post_order
    def Post_order(self,root):
        if root is not None:

            self.Post_order(root.left)
            self.Post_order(root.right)
            print(root.data, end=' ')

    # Tree_high
    def Tree_high(self,root):
        if root is None:
            return -1
        return max(self.Tree_high(root.left),self.Tree_high(root.right))+1

tree = Tree()
root = tree.createNode(30)

print("root ---->>",root.data)
tree.insert(root,25)
tree.insert(root,35)
tree.insert(root,22)
tree.insert(root,26)


print('Inorder----->')

tree.Pre_order(root)
print()
tree.Post_order(root)
print()
tree.tree_INorder(root)
print()
print(tree.Tree_high(root))










