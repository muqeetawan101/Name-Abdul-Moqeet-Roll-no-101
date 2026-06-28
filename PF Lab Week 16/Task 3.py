try:
    file = open("student.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")