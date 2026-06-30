# Lambda function to find the square of a number

square = lambda x: x ** 2

num = int(input("Enter a number: "))

result = square(num)

print("Square of", num, "is", result)