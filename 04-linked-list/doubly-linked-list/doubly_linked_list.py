class LinkedListNode:

  def __init__(self, data):
    self.data = data
    self.next = None
    self.back = None


class LinkedListIterator:

  def __init__(self, node=None):
    self.currentNode = node

  def data(self):
    return self.currentNode.data

  def next(self):
    self.currentNode = self.currentNode.next
    return self

  def current(self):
    return self.currentNode


class DoubleLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None

  def begin(self):
    itr = LinkedListIterator(self.head)
    return itr

  def printList(self):
    itr = self.begin()
    while itr.current() is not None:
      print(itr.data(), "->", end=" ")
      itr.next();
    print()

  def find(self, data):
    for itr in self.begin():
      if data == itr.data():
        return itr.current()
    return None

  def insertAfter(self, node, data):
    new_node = LinkedListNode(data)
    new_node.next = node.next
    new_node.back = node
    node.next = new_node

    if new_node.next is None:
      self.tail = new_node
    else:
      new_node.next.back = new_node

  def insertLast(self, data):
    new_node = LinkedListNode(data)

    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.back = self.tail
      self.tail.next = new_node
      self.tail = new_node

  def insertBefore(self, node, data):
    new_node = LinkedListNode(data)
    new_node.next = node

    if node is self.head:
      self.head = new_node
    else:
      node.back.next = new_node

    node.back = new_node

  def deleteNode(self, node):
    if self.head is self.tail:
      self.head = None
      self.tail = None
    elif node.back is None:
      self.head = node.next
      node.next.back = None
    elif node.next is None:
      self.tail = node.back
      node.back.next = None
    else:
      node.back.next = node.next
      node.next.back = node.back
      node = None
