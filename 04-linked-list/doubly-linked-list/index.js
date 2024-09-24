const { DoubleLinkedList } = require("./doublylinkedlist.js");

let list = new DoubleLinkedList();
list.insertLast(1);
list.insertLast(2);
list.insertLast(3);
list.printList();

list.insertAfter(list.find(2), 98);
list.printList();

list.deleteNode(list.find(2));
list.printList();

list.insertBefore(list.find(98), 76);
list.printList();

list.deleteNode(list.find(1));
list.printList();
