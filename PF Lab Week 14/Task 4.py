# Mixed example using os, __main__, and is

import os

def show_directory():
    print("Current Directory:", os.getcwd())
    print("Items:", os.listdir())

def compare_objects():
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    print("a is b:", a is b)
    print("a is c:", a is c)
    print("a == c:", a == c)

if __name__ == "__main__":
    show_directory()
    print()
    compare_objects()