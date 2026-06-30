def sum_numbers(n):

    if n == 0:
        return 0

    return n + sum_numbers(n - 1)

number = int(input("Enter a number: "))

print("Sum =", sum_numbers(number))