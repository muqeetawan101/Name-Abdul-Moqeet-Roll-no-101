# Convert Celsius to Fahrenheit using map()

celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)