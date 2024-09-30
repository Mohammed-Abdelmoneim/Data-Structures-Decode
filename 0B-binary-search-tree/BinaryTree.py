from collections import deque

class TreeNode:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class NodeAndParent:

  def __init__(self, node=None, parent=None, isLeft=None):
    self.node = node
    self.parent = parent
    self.isLeft = isLeft


class BinaryTree:

  def __init__(self):
    self.root = None
  
  def balance(self):
    # Create a list to store the tree nodes in order
    nodes = []
    self.inOrderToArray(self.root, nodes)
    # Rebuild the tree with balanced nodes
    self.root = self.recursiveBalance(0, len(nodes) - 1, nodes)

  def inOrderToArray(self, node, nodes):
    if node is None:
      return
    # Traverse the left subtree
    self.inOrderToArray(node.left, nodes)
    # Add the node data to the list
    nodes.append(node.data)
    # Traverse the right subtree
    self.inOrderToArray(node.right, nodes)

  def recursiveBalance(self, start, end, nodes):
    if start > end:
      return None
    # Find the middle node and use it as the root of the subtree
    mid = (start + end) // 2
    newNode = TreeNode(nodes[mid])
    # Recursively build the left and right subtrees
    newNode.left = self.recursiveBalance(start, mid - 1, nodes)
    newNode.right = self.recursiveBalance(mid + 1, end, nodes)
    return newNode
    
  def isExist(self, data):
    return self.bsFind(data) is not None

  def findNodeAndParent(self, data):
    currentNode = self.root
    parent = None
    nodeAndParentInfo = None
    isLeft = False
    while currentNode is not None:
      if currentNode.data == data:
        nodeAndParentInfo = NodeAndParent(currentNode, parent, isLeft)
        break
      elif currentNode.data > data:
        parent = currentNode
        isLeft = True
        currentNode = currentNode.left
      else:
        parent = currentNode
        isLeft = False
        currentNode = currentNode.right
    return nodeAndParentInfo

  def bsFind(self, data):
    currentNode = self.root
    while currentNode is not None:
      if currentNode.data == data:
        return currentNode
      elif currentNode.data > data:
        currentNode = currentNode.left
      else:
        currentNode = currentNode.right
    return None
  
  def bsDelete(self, data):
    nodeAndParentInfo = self.findNodeAndParent(data)
    if nodeAndParentInfo.node is None:
      return
    # Node has two children
    if nodeAndParentInfo.node.left is not None and nodeAndParentInfo.node.right is not None:
      self.bsDeleteHasChilds(nodeAndParentInfo.node)
    # Node has one child
    elif nodeAndParentInfo.node.left is not None or nodeAndParentInfo.node.right is not None:
      self.bsDeleteHasOneChild(nodeAndParentInfo.node)
    # Node is a leaf
    else:
      self.bsDeleteLeaf(nodeAndParentInfo)

  def bsDeleteLeaf(self, nodeAndParentInfo):
    if nodeAndParentInfo.parent is None:
      self.root = None
    else:
      if nodeAndParentInfo.isLeft:
        nodeAndParentInfo.parent.left = None
      else:
        nodeAndParentInfo.parent.right = None

  def BSDelete_Has_One_Child(nodeToDelete):
    # Find the node to replace the deleted node with
    nodeToReplace = None
    if nodeToDelete.left != None:
      nodeToReplace = nodeToDelete.left
    else:
      nodeToReplace = nodeToDelete.right

    # Replace the deleted node with the replacement node
    nodeToDelete.data = nodeToReplace.data
    nodeToDelete.left = nodeToReplace.left
    nodeToDelete.right = nodeToReplace.right

  def BSDelete_Has_Childs(nodeToDelete):
    # Find the node to replace the deleted node with
    currentNode = nodeToDelete.right
    parent = None
    while currentNode.left != None:
      parent = currentNode
      currentNode = currentNode.left
    # Replace the deleted node with the replacement node
    if parent != None:
      parent.left = currentNode.right
    else:
      nodeToDelete.right = currentNode.right
    nodeToDelete.data = currentNode.data
    
    
  def BSInsert(self, data):
    newNode = TreeNode(data)
    if self.root is None:
      self.root = newNode
      return
    currentNode = self.root
    while currentNode is not None:
      if currentNode.data > data:
        if currentNode.left is None:
          currentNode.left = newNode
          break
        else:
          currentNode = currentNode.left
      else:
        if currentNode.right is None:
          currentNode.right = newNode
          break
        else:
          currentNode = currentNode.right
          
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
