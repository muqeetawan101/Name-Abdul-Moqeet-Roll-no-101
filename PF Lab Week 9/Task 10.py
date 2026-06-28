total = 0

for i in range(1, 6):
    marks = int(input("Enter marks of student " + str(i) + ": "))
    total += marks

average = total / 5

print("Total Marks =", total)
print("Average Marks =", average)