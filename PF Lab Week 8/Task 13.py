username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin":
    if password == "admin123":
        print("Welcome Admin")
    else:
        print("Incorrect Password")

elif username == "judge":
    if password == "judge123":
        print("Welcome Judge")
    else:
        print("Incorrect Password")

elif username == "lawyer":
    if password == "lawyer123":
        print("Welcome Lawyer")
    else:
        print("Incorrect Password")

elif username == "client":
    if password == "client123":
        print("Welcome Client")
    else:
        print("Incorrect Password")

else:
    print("User Not Found")