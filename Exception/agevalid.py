"""Q.6 Age Validation
Accept the user's age as input. Handle invalid input and display the age if it is a valid integer."""


try:
	a=int(input("Enter age = "))
	print("age = ",a)
    
except ValueError:
	print("valid Integer")