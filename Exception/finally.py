"""Q5. Using finally
Write a Python program to divide two numbers and display "Program Completed" using the finally block, whether an exception occurs or not."""


try:
	num1=int(input("Enter number1 = "))
	num2=int(input("Enter number2 = "))
	print( num1 / num2)
	
except ZeroDivisionError:
	print("can not divide zero")
	
finally:
	print("Program Completed")