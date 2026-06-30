total = 0
count = 1

while count <= 5:
    marks = float(input("Enter marks of Student " + str(count) + ": "))
    total += marks
    count += 1

average = total / 5

print("\nTotal Marks =", total)
print("Average Marks =", average)

if average >= 90:
    print("Grade: A+")
elif average >= 80:
    print("Grade: A")
elif average >= 70:
    print("Grade: B")
else:
    print("Need Improvement")