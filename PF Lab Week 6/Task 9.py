numbers = [12, 45, 8, 67, 23, 90, 34]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest Number =", largest)