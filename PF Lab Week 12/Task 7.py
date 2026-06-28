def table(number):

    print("Table of", number)

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

num = int(input("Enter a number: "))
table(num)