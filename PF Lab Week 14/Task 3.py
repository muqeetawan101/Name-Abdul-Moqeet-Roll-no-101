# Demonstrating the 'is' operator

list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)

print("list1 == list3:", list1 == list3)