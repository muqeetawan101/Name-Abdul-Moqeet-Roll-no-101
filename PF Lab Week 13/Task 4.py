# Filter even numbers

numbers = [5, 8, 11, 14, 19, 22, 25, 28]

evens = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", evens)