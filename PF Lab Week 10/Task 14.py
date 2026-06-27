students = {}

for i in range(3):
    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    students[name] = marks

print("\nStudent Records:")

for name, marks in students.items():
    print(name, ":", marks)

highest = max(students, key=students.get)

print("\nTop Student:", highest)
print("Marks:", students[highest])