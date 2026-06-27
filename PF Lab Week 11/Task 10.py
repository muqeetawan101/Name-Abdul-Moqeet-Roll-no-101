library = {"Python", "Java", "C++", "Database"}

while True:

    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Display Books")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        library.add(book)
        print("Book Added.")

    elif choice == "2":
        book = input("Enter book name: ")

        if book in library:
            library.remove(book)
            print("Book Removed.")
        else:
            print("Book Not Found.")

    elif choice == "3":
        print("\nAvailable Books:")
        for book in library:
            print(book)

    elif choice == "4":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")