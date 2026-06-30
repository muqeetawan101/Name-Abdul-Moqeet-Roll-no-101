# Sorting tuples using lambda

students = [
    ("Ali", 82),
    ("Ahmed", 75),
    ("Sara", 91),
    ("Ayesha", 88)
]

sorted_students = sorted(students, key=lambda x: x[1])

print("Sorted by Marks:")
for student in sorted_students:
    print(student)