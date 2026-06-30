def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Answer =", power(base, exponent))