"""2.Find the Maximum Element
Write a Python program to create a set of integers and find the largest element in the set."""


n=int(input("Enter number of element = "))

maximum = 0

for i in range(n):
    x=int(input("Enter element = "))
    if x > maximum:
	    maximum = x
    else:
        x > maximum
print("largest element in set = ",maximum)