## Binary Search Tree

This properties what makes binary search tree a **binary search tree**.
why: by divide it to levels we make the search **faster**, the number of levels is less than the number of items (n), and the **optimum** number of levels is log(n) (Balanced) but not always.
![binary search tree](binary-search-tree.png)

### Duplication Handling

![Duplication Handling](duplication-handling.png)

### Insert

![insert](insert.png)
![insert order](insert-order.png)

### Find

![Find](find.png)

### Delete

There are three cases
![Delete](delete.png)

![Delete](delete1.png)
![Delete](delete2.png)
![Delete](delete3.png)
![Delete](delete4.png)
![Delete](delete5.png)
![Delete](delete6.png)

Turn this into Pseudo Code
![algo](delete-algo.png)

Node has one child: we delete and replaced 5 by 6 in the below image
![delete one](delete-one.png)

Node is a leaf
![delete leaf](delete-leaf.png)

### Balance

![balance](balance.png)
![balance algo](balance-algo.png)
