class LinkedListNode {
  constructor(data) {
    this.data = data; // the data value stored in the node
    this.next = null; // a reference to the next node in the list
  }
}
class LinkedListIterator {
  constructor(node) {
    this.currentNode = node;
  }

  data() {
    if (this.currentNode == null) return null;
    return this.currentNode.data;
  }

  next() {
    if (this.currentNode != null) {
      this.currentNode = this.currentNode.next;
    }
    return this;
  }

  current() {
    return this.currentNode;
  }
}
class SingleLinkedList {
  constructor() {
    this.length = 0;
    this.head = null;
    this.tail = null;
  }

  addHead(node) {
    this.head = node;
    this.tail = node;
  }

  // canInsert(_data) {
  //   if (this.unique && this.isExist(_data)) {
  //     console.log(_data, "already exist!");
  //     return false;
  //   } else {
  //     return true;
  //   }
  // }

  insertLast(_data) {
    // if (!canInsert(_data)) return;

    const newNode = new LinkedListNode(_data);
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
  }

  insertAfter(node, _data) {
    //if (!canInsert(_data)) return;

    const newNode = new LinkedListNode(_data);
    newNode.next = node.next;
    node.next = newNode;
    if (newNode.next === null) {
      this.tail = newNode;
    }
    this.length++;
  }

  deleteNode(node) {
    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
    } else if (this.head === node) {
      this.head = node.next;
    } else {
      const parentNode = this.findParent(node);

      if (this.tail === node) {
        this.tail = parentNode;
      } else {
        parentNode.next = node.next;
      }
    }
    this.length--;
  }

  deleteNodeByData(_data) {
    const node = this.find(_data);
    if (node === null) {
      return;
    }
    this.deleteNode(node);
  }

  deleteHead() {
    if (this.head === null) {
      return;
    }
    this.deleteNode(this.head);
  }

  insertBefore(node, _data) {
    //if (!canInsert(_data)) return;
    const newnode = new LinkedListNode(_data);
    newnode.next = node;

    const parentNode = this.findParent(node);

    if (parentNode === null) {
      this.head = newnode;
    } else {
      parentNode.next = newnode;
    }
    this.length++;
  }

  find(_data) {
    for (let itr = this.begin(); itr.current() !== null; itr.next()) {
      if (itr.data() === _data) {
        return itr.current();
      }
    }
    return null;
  }

  findParent(node) {
    for (let itr = this.begin(); itr.current() !== null; itr.next()) {
      if (itr.current().next === node) {
        return itr.current();
      }
    }
    return null;
  }

  getLengthItr() {
    let count = 0;
    for (let itr = this.begin(); itr.current() !== null; itr.next()) {
      count++;
    }
    return count;
  }

  size() {
    return this.length;
  }

  printList() {
    let output = "";
    for (let itr = this.begin(); itr.current() !== null; itr.next()) {
      output += itr.data() + " -> ";
    }
    console.log(output);
  }

  sum() {
    let sum = 0;
    for (let itr = this.begin(); itr.current() !== null; itr.next()) {
      sum += itr.data();
    }
    return sum;
  }
  begin() {
    const itr = new LinkedListIterator(this.head);
    return itr;
  }
}

module.exports = {
  SingleLinkedList: SingleLinkedList,
  LinkedListNode: LinkedListNode,
  LinkedListIterator: LinkedListIterator,
};
