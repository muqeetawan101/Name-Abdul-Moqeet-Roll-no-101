balance = 5000
withdraw = 3000
pin = 1234
entered_pin = 1234

if entered_pin == pin:
    if withdraw <= balance:
        balance = balance - withdraw
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
else:
    print("Incorrect PIN")