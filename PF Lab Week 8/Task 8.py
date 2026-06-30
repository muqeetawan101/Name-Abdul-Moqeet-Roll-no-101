students = set()

for i in range(5):
    name = input("Enter student name: ")
    students.add(name)

print("\nRegistered Students:")

for student in students:
    print(student)

print("Total Students:", len(students))