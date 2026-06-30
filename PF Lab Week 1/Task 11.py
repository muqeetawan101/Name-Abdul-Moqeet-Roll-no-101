password = "Python123"

if len(password) >= 8:
    if any(char.isdigit() for char in password):
        print("Strong Password")
    else:
        print("Password must contain at least one number.")
else:
    print("Password is too short.")