number = int(input("Enter a three-digit number: "))

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

reverse = (ones * 100) + (tens * 10) + hundreds

print("Reversed Number =", reverse)