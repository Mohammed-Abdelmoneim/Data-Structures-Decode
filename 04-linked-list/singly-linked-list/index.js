const {
  SingleLinkedList,
  LinkedListIterator,
  LinkedListNode,
} = require("./singlylinkedlist.js");

let singlelist = new SingleLinkedList();
singlelist.insertLast(1);
singlelist.insertLast(2);
singlelist.insertLast(3);
singlelist.printList();

singlelist.insertAfter(singlelist.find(2), 98);
singlelist.printList();

singlelist.deleteNode(singlelist.find(2));
singlelist.printList();

singlelist.insertBefore(singlelist.find(98), 76);
singlelist.printList();

singlelist.deleteNode(singlelist.find(1));
singlelist.printList();
