fruits = ("Apple", "Banana", "Orange", "Mango")

fruit = input("Enter fruit name: ")

if fruit in fruits:
    print("Index =", fruits.index(fruit))
else:
    print("Fruit not found.")