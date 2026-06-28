correct_password = "python123"

for user in range(1, 4):

    print("\nUser", user)

    for attempt in range(1, 4):

        password = input("Attempt " + str(attempt) + ": ")

        if password == correct_password:
            print("Login Successful")
            break
        else:
            print("Incorrect Password")