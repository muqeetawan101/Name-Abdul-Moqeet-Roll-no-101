total = 0

for customer in range(1, 4):

    print("\nCustomer", customer)

    for item in range(1, 3):
        price = float(input("Enter Item Price: "))
        total += price

print("\nTotal Bill =", total)