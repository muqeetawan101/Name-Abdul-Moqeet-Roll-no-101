# Using lambda with map()

numbers = [2, 4, 6, 8, 10]

doubled = list(map(lambda x: x * 2, numbers))

print("Original List:", numbers)
print("Doubled List:", doubled)