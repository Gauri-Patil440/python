"""Q.1
Student Marks Dictionary
Write a Python program to take a student name and marks as input and store them in a dictionary. 
Display the student name and marks."""


student = {}

name = input("Enter student name: ")

marks = int(input("Enter student marks: "))

student[name] = marks

print("Student Dictionary =", student)

print("Student Name =", name)
print("Student Marks =", marks)