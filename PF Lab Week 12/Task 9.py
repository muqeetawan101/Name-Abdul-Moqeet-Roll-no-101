marks = 90

def update_marks():
    marks = 75
    print("Marks inside function:", marks)

update_marks()

print("Marks outside function:", marks)
print("Global variable remains the same.")