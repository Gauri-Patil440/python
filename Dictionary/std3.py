"""Q.5 Dictionary Update
Write a Python program to create a dictionary containing three key-value pairs. 
Ask the user for a key and a new value, then update the dictionary with the new value. 
Display the updated dictionary."""


student = {}
for i in range(3):
    key = input("enter key = ")
	value = int(input("enter value = "))

    student[key] = value

print("Original Dictionary =", student)

key = input("Enter key to update = ")
value = int(input("Enter new value = "))

student[key] = value

print("Updated Dictionary =", student)