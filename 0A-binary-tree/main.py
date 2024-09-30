from BinaryTree import BinaryTree

# create a new binary tree
tree = BinaryTree()

# insert elements into the tree
tree.Insert(1)
tree.Insert(2)
tree.Insert(3)
tree.Insert(4)
tree.Insert(5)
tree.Insert(6)
tree.Insert(7)

# print the height of the tree
print("Height: ", tree.height())

# traverse the tree in pre-order
tree.PreOrder()

# traverse the tree in in-order
tree.InOrder()

# traverse the tree in post-order
tree.PostOrder()
