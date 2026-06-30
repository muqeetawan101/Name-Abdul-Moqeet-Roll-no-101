def even_odd(number):

    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

num = int(input("Enter a number: "))
even_odd(num)