# Keep only positive numbers

numbers = [-10, 15, -5, 20, 30, -8, 12]

positive = list(filter(lambda x: x > 0, numbers))

print("Positive Numbers:", positive)