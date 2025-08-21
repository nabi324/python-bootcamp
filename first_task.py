# Create a Python program that allows a user to enter their name and some notes, then saves the notes to a file and displays them.
 # This task will help you practice input/output operations, variables, and file handling.

name = input("Enter your name: ")
age = input("Enter your age: ")
major = input("Enter your major: ")
hobby = input("Enter your hobby: ")

file_name = f"notes.txt"

with open(file_name, "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}\n")
    f.write(f"Major: {major}\n")
    f.write(f"Hobby: {hobby}\n")

print("Your notes have been saved, and here is the content of the file:")
with open(file_name, "r") as f:
    print(f.read())
