# Define the singly linked list node class
class LinkedListNode:

  def __init__(self, data):
    self.data = data
    self.next = None


# Define the linked list iterator class
class LinkedListIterator:

  def __init__(self, node=None):
    self.currentNode = node

  # Return the current node's data
  def data(self):
    return self.currentNode.data

  # Advance to the next node and return the iterator
  def next(self):
    self.currentNode = self.currentNode.next
    return self

  # Return the current node
  def current(self):
    return self.currentNode


# Define the single linked list class
class SingleLinkedList:

  def __init__(self):
    self.length = 0
    self.head = None
    self.tail = None

  # Add a node to the head of the list
  def addHead(self, node):
    self.head = node
    self.tail = node

  # Insert a new node at the end of the list
  def insertLast(self, data):
    newNode = LinkedListNode(data)
    if self.head is None:
      self.head = newNode
      self.tail = newNode
    else:
      self.tail.next = newNode
      self.tail = newNode
    self.length += 1

  # Insert a new node after a given node
  def insertAfter(self, node, data):
    newnode = LinkedListNode(data)
    newnode.next = node.next
    node.next = newnode
    if newnode.next is None:
      self.tail = newnode
    self.length += 1

  # Delete a given node from the list
  def deleteNode(self, node):
    if self.head == self.tail:
      self.head = None
      self.tail = None
    elif self.head == node:
      self.head = node.next
    else:
      parentNode = self.findParent(node)

      if self.tail == node:
        self.tail = parentNode
      else:
        parentNode.next = node.next
    self.length -= 1

  # Delete the first node in the list
  def deleteHead(self):
    if self.head is None:
      return
    self.deleteNode(self.head)

  # Insert a new node before a given node
  def insertBefore(self, node, data):
    newnode = LinkedListNode(data)
    newnode.next = node

    parentNode = self.findParent(node)

    if parentNode is None:
      self.head = newnode
    else:
      parentNode.next = newnode
    self.length += 1

  # Find a node with the given data value
  def find(self, data):
    itr = self.begin()
    while itr.current() is not None:
      if itr.data() == data:
        return itr.current()
      itr.next()
    return None

  # Find the parent of a given node
  def findParent(self, node):
    itr = self.begin()
    while itr.current() is not None:
      if itr.current().next == node:
        return itr.current()
      itr.next()
    return None

  # Return the length of the list using an iterator
  def getLengthItr(self):
    count = 0
    itr = self.begin()
    while itr.current() is not None:
      count += 1
      itr.next()
    return count

  # Return the length of the list
  def Length(self):
    return self.length

  # Print the contents of the list
  def printList(self):
    itr = self.begin()
    while itr.current() is not None:
      print(itr.data(), "->", end=" ")
      itr.next()

  def printList(self):
    itr = self.begin()
    while itr.current() != None:
      print(itr.data(), end=" -> ")
      itr.next()
    print()

  def sum(self):
    sum = 0
    itr = self.begin()
    while itr.current() != None:
      sum += itr.data()
      itr.next()
    return sum

  def begin(self):
    itr = LinkedListIterator(self.head)
    return itr
