"""Q.7 Password Length Check
Accept a password from the user. If the password contains fewer than six characters, raise a ValueError 
and handle it using try-except."""


try:
	a=input("Enter password = ")
	print("password = ",a)
	if len(a)<6:
		raise ValueError
	print("valid password")
	
except ValueError:
	print("enter 6 characters password")