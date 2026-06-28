students = {
    101: "Ali",
    102: "Ahmed",
    103: "Sara"
}

roll = int(input("Enter Roll Number: "))

if roll in students:
    print("Student Name:", students[roll])
else:
    print("Record not found.")