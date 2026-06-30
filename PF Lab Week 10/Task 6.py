def count_digits(number):

    if number < 10:
        return 1

    return 1 + count_digits(number // 10)

number = int(input("Enter a number: "))

print("Number of Digits =", count_digits(number))