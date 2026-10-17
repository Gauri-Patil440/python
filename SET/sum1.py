"""1. Find the Sum of All Elements in a Set
Write a Python program to create a set of integers and calculate the sum of all elements."""

n=int(input("Enter number of elements = "))

sum=0

for i in range(n):
   x=int(input("Enter the elements = "))
   sum = sum + x
print("sum of elements =",sum)