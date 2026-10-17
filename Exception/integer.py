"""Q2. Integer Input
Write a Python program to accept an integer from the user. Handle the exception if the user enters a non-numeric value."""


try:
    num=int(input("Enter the Integer ="))
    print("user integer = ",num)
	
except TypeError:
    print("Enter valid integer")