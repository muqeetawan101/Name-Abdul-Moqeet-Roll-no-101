marks = []

for i in range(5):
    mark = int(input("Enter marks of student " + str(i + 1) + ": "))
    marks.append(mark)

print("Marks List:", marks)
print("Highest Marks:", max(marks))
print("Average Marks:", sum(marks) / len(marks))