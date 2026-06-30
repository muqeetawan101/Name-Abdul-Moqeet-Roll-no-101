# Lambda function to calculate simple interest

interest = lambda p, r, t: (p * r * t) / 100

principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate (%): "))
time = float(input("Enter Time (years): "))

print("Simple Interest =", interest(principal, rate, time))