def largest(a, b, c):

    if a >= b and a >= c:
        print("Largest Number =", a)

    elif b >= a and b >= c:
        print("Largest Number =", b)

    else:
        print("Largest Number =", c)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

largest(x, y, z)