## Hash Table

Is a dictionary or **KeyValue** Pairs put with a twist.

- It's preferred **not mandatory** to make all keys and values from the same type

This is the activity diagram for the dictionary set function, the twist here is that with hash table **we can make "search for key" process to be o(1)**
![search for key](search-key.png)

hash table mechanism is from the key itself we can know its place or where it should be placed, this can be done by the normal hash function that uses the modulus (%)
![how it works](how-it-works.png)
![hashing](hashing.png)
![hash table](hashtable.png)

## COllision Handling

- Linear Probing
  ![Linear Probing](linear-probing.png)
- double-probing.png Probing
  ![Quadratic Probing](quadratic-probing.png)
- Double Hashing: orange color is hash2
  ![Double Probing](double-probing.png)
- Separate Chaining: make it a linked list, easy!
  ![Separate Chaining](separate-chaining.png)

### Open/Closed Addressing & Open/Closed Hashing

![types](types.png)

### Implementation

![infrastructure](hashtable-operation.png)
![hash](hash.png)
![collision handling](collision-handling.png)
set
![add to entries / set](addToEntries.png)
![resize or not](ResizeOrNot.png)
![set](set.png)

Note: it's just not recommended but you can use it, it's like recurison, and here we have a base case in the below image to break the loop or clog infinity call.
![circular](circular.png)

Here's the solution
![circular solution](circular-resolution.png)

![get](get.png)
