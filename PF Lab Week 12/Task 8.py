def binary(n):

    if n > 1:
        binary(n // 2)

    print(n % 2, end="")

number = int(input("Enter a decimal number: "))

print("Binary =", end=" ")
binary(number)