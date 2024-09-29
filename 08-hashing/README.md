## Hashing

The practice of transforming a given key or string of characters into another value for the purpose of security. Unlike standard encryption, hashing is always used for **one-way encryption**, and hashed values are very difficult to decode.
![hash](hash.png)

- it's **not an encryption** excatly

> Hash Function: The function that turns input into a hash  
> ![hash function](hash-function.png)

> The simplest known Hash function
> ![simple hash](simple-hash.png)

### Terms

![terms](terms.png)

### Notes

- This is a Hex decimal output function (hash 32): which is each 2 value is 1 Byte
  ![fnv-1a](FNV-1a.png)

- Hash is **Case Sensitive**: any simple change will change the hash value
  ![case-sensitive](case-sensitive.png)

![fnv-1a algo](FNV-1a-algo.png)
![xor](xor.png)
![xor az](xor-az.png)

### Collision

If the hash function takes deferent inputs but output the same hash
![Collision](collision.png)

## Hashing Usage

![hashing usage](hashing-usage.png)
