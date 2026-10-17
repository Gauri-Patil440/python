"""Q.2
Employee Salary Record
Write a Python program to take an employee ID and salary as input and store them in a dictionary. 
Display the employee ID and salary."""


employee={}

Id = input("Enter Employee ID = ")
salary = input("Enter employee salary = ")

employee[Id] = salary

print("employee Dictionary = ",employee)
print("employee ID = ",Id)
print("employee salary = ",salary)

