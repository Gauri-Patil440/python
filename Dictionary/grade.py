"""Q.6
Student Grade Dictionary
Write a Python program to take a student's name and percentage as input. Store the student's name and 
grade in a dictionary based on the following criteria:
75 and above → A
60 to 74     → B
40 to 59     → C
Below 40     → Fail"""



student = {}

name = input("Enter student name = ")
percentage = int(input("Enter percentage = "))

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

student[name] = grade

print("Student Name =", name)
print("Percentage =", percentage)
print("Grade =", grade)
print("Student Dictionary =", student)