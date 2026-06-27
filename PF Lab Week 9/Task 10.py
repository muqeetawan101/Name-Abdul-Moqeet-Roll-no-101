def login(username, password):

    if username == "admin" and password == "admin123":
        print("Login Successful")

    else:
        print("Invalid Username or Password")

user = input("Enter Username: ")
pwd = input("Enter Password: ")

login(user, pwd)