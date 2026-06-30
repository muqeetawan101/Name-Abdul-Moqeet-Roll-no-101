# Filter numbers greater than 50

marks = [45, 78, 52, 39, 91, 67, 48]

passed = list(filter(lambda x: x > 50, marks))

print("Marks Above 50:", passed)