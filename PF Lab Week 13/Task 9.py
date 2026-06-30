from functools import reduce

numbers = [45, 67, 12, 89, 34]

maximum = reduce(lambda a, b: a if a > b else b, numbers)

print("Maximum Number =", maximum)