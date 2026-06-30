students = 3
subjects = 4

for i in range(1, students + 1):

    print("\nStudent", i)

    total = 0

    for j in range(1, subjects + 1):
        marks = int(input("Enter marks of Subject " + str(j) + ": "))
        total += marks

    average = total / subjects

    print("Total Marks =", total)
    print("Average =", average)

    if average >= 80:
        print("Grade: A")

    elif average >= 70:
        print("Grade: B")

    elif average >= 60:
        print("Grade: C")

    else:
        print("Fail")