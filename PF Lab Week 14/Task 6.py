courses = {"Python", "Java", "C++", "AI"}

course = input("Enter course name: ")

if course in courses:
    print(course, "is available.")
else:
    print(course, "is not available.")