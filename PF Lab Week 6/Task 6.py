balance = 5000

def deposit():
    global balance
    amount = 1500
    balance = balance + amount
    print("Deposited:", amount)

deposit()
print("Current Balance:", balance)