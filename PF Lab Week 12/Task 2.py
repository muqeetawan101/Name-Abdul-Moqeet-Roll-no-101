# Lambda function to find the greater of two numbers

greater = lambda a, b: a if a > b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Greater number is:", greater(num1, num2))