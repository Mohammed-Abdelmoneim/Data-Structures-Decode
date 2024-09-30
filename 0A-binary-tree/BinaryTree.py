from collections import deque

class TreeNode:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:

  def __init__(self):
    self.root = None

  def Insert(self, data):
    newNode = TreeNode(data)
    if self.root is None:
      self.root = newNode
      return
    q = deque()
    q.append(self.root)
    while q:
      currentNode = q.popleft()
      if currentNode.left is None:
        currentNode.left = newNode
        break
      else:
        q.append(currentNode.left)

      if currentNode.right is None:
        currentNode.right = newNode
        break
      else:
        q.append(currentNode.right)

  def height(self):
    return self.internal_height(self.root)

  def internal_height(self, node):
    if node is None:
      return 0
    return 1 + max(self.internal_height(node.left),
                   self.internal_height(node.right))

  def PreOrder(self):
    self.internalPreOrder(self.root)
    print()

  def internalPreOrder(self, node):
    if node is None:
      return
    print(node.data, "->", end=" ")
    self.internalPreOrder(node.left)
    self.internalPreOrder(node.right)

  def InOrder(self):
    self.internalInOrder(self.root)
    print("")

  def internalInOrder(self, node):
    if node is None:
      return
    self.internalInOrder(node.left)
    print(node.data, " -> ", end='')
    self.internalInOrder(node.right)

  def PostOrder(self):
    self.internalPostOrder(self.root)
    print()

  def internalPostOrder(self, node):
    if node is None:
      return
    self.internalPostOrder(node.left)
    self.internalPostOrder(node.right)
    print(node.data, "->", end=" ")
