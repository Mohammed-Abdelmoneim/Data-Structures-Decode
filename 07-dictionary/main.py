from Dictionary import Dictionary

dic = Dictionary()
dic.print()
dic.set("Sinar", "sinar@gmail.com")
dic.set("Elvis", "elvis@gmail.com")
dic.print()

dic.set("Tane", "tane@gmail.com")
dic.set("Gerti", "gerti@gmail.com")
dic.set("Arist", "arist@gmail.com")
dic.print()

print(dic.get("Tane"))
print(dic.get("Sinar"))
print(dic.get("Elviaaa"))

dic.remove("Sinar")
dic.remove("Elvis")
dic.remove("Tane")
dic.remove("Gerti")
dic.remove("Arist")
dic.print()

dic.set("Sinar", "sinar@gmail.com")
dic.print()
