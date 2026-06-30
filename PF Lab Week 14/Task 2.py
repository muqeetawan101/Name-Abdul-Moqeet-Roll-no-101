# Demonstrating __name__ == "__main__"

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("Addition:", add(x, y))
    print("Multiplication:", multiply(x, y))