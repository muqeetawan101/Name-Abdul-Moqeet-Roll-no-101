balance = 5000

while True:
    amount = int(input("Enter withdrawal amount (0 to Exit): "))

    if amount == 0:
        print("Thank you for using the ATM.")
        break

    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")