## Singly Linked Lists

A Singly Linked List is a data structure consisting of a sequence of items (objects or nodes), where each item contains data and a pointer (reference) to the next item (node) in the sequence.

![linked list](linked-list.png)

> How the node looks like? ![one node](node.png)
> Linked list infrastructure and operations ![linked list details](details.png) > ![linked list diagram](linkedlist-diagram.png)

### Singly Linked List Implementation

> ![insert last](insertlast.png)

> ![how it will be done](insert-after.png) ![insert after](insert-after-algo.png)

> [!TIP]
> If you are working with Linked lists or do operations on them, its preferred to visualize or draw (pen and paper) the items and then use this drawing to write the steps or algorithm or **the code itself**.

> ![insert before](insert-before.png) > ![delete](delete-node.png) > ![delete algo](delete-node-algo.png)

## Doubly Linked Lists

Similar to a Singly Linked List, **However**, it has two pointers: one pointing to the next item and another pointing to the previous item in the sequence.

> Here we can call it: back, previous or parent .. etc.

> ![doubly linked list node](doubly-linkedlist.png)

> - Unlike Singly Linked Lists, in the node we add pointer to the back or previous node.
> - And we remove findParent because we already have it in the node itself.
>   ![doubly linkedlist diagram](doubly-linkedlist-diagram.png)

> **Insert after** ![insert after](doubly-insert-after.png) ![insert after algo](doubly-insert-after-algo.png)

> **Insert last** ![insert last](doubly-insert-last.png) ![insert last algo](doubly-insert-last-algo.png)

> **Delete Node** ![delete node](doubly-delete.png) ![delete node 2](doubly-delete2.png) ![delete node algo](doubly-delete-algo.png)

### Exercises

- Use Generic Types (to accept any data type).
- Get length from property not from function (update when delete or insert).
- Copy List (to new list not to assign the address).
