numbers = [10, 20, 30, 40, 50]

search = int(input("Enter number to search: "))

if search in numbers:
    print(search, "found in the list.")
else:
    print(search, "not found in the list.")