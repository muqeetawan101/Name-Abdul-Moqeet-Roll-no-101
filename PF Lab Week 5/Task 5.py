def grade(marks):

    if marks >= 90:
        return "A+"

    elif marks >= 80:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 60:
        return "C"

    else:
        return "Fail"

marks = int(input("Enter Marks: "))

print("Grade =", grade(marks))