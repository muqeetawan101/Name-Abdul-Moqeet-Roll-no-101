def simple_interest(principal, rate, time):

    interest = (principal * rate * time) / 100
    return interest

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest =", simple_interest(p, r, t))