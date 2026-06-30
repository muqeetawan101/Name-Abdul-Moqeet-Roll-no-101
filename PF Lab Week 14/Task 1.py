# Using the os library

import os

print("Current Working Directory:")
print(os.getcwd())

folder = "MyFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Folder created successfully.")
else:
    print("Folder already exists.")

print("Files and Folders in Current Directory:")
print(os.listdir())