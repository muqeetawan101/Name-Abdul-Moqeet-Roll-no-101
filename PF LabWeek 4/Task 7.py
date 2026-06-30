for student in range(1, 4):

    total = 0
    print("\nStudent", student)

    for subject in range(1, 4):
        marks = int(input("Enter marks of Subject " + str(subject) + ": "))
        total += marks

    average = total / 3
    print("Total =", total)
    print("Average =", average)