# Using lambda with filter()

numbers = [11, 14, 17, 20, 23, 26, 29, 32]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original List:", numbers)
print("Even Numbers:", even_numbers)