a=int(input("Enter number of students: "))
for i in range(a):
    y=input("Enter student name: ")
    z=input("Enter his age: ")
    x=input("Enter his roll no: ")
    print("Student name is ",y)
    print("Student age is ",z)
    print("Student roll no is ",x)
    x = int(input("Enter total numbers: "))
    y = int(input("Enter obtained marks: "))
    per = y * 100 / x
    print(per)
    if per >= 90:
        grade = "A"
    elif per >= 85:
        grade = "A-"
    elif per >= 80:
        grade = "B+"
    elif per >= 75:
        grade = "B"
    elif per >= 70:
        grade = "B-"
    elif per >= 65:
        grade = "C+"
    elif per >= 60:
        grade = "C"
    elif per >= 55:
        grade = "C-"
    elif per >= 50:
        grade = "D+"
    elif per >= 45:
        grade = "D"
    elif per >= 40:
        grade = "D-"
    else:
        grade = "F"
    print(grade)