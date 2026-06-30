total = 0

while True:
    item = input("Enter Item Name (or 'done' to finish): ")

    if item.lower() == "done":
        break

    price = float(input("Enter Price: "))
    total += price

print("\nTotal Bill =", total)

if total > 5000:
    discount = total * 0.10
    total -= discount
    print("10% Discount Applied!")

print("Final Bill =", total)