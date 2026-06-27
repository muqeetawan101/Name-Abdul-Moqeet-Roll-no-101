name = input("Enter student name: ")

marks1 = float(input("Enter marks of English: "))
marks2 = float(input("Enter marks of Math: "))
marks3 = float(input("Enter marks of Science: "))

total = marks1 + marks2 + marks3
percentage = (total / 300) * 100

print("Student:", name)
print("Total Marks:", total)
print("Percentage:", percentage, "%")