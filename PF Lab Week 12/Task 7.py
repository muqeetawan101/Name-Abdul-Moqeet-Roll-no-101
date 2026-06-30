# Lambda function to check even or odd

check = lambda n: "Even" if n % 2 == 0 else "Odd"

number = int(input("Enter a number: "))

result = check(number)

print("The number is:", result)