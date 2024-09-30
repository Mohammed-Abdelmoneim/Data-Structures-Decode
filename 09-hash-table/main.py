from HashTable import HashTable

table = HashTable()
table.print()
table.set("Sinar", "sinar@gmail.com")
table.set("Elvis", "elvis@gmail.com")
table.set("Tane", "tane@gmail.com")
table.print()
print("[get] " + table.get("Sinar"))
table.set("Gerti", "gerti@gmail.com")
table.set("Arist", "arist@gmail.com")
table.print()
print("[get] " + table.get("Sinar"))
