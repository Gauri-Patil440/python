"""Question 7: Write a Java program to handle InputMismatchException.

Accept integer input from the user. If the user enters a character instead of an integer, handle exceptions.
Asked In Practice Assignment
Input:
Enter number: A

Output:
Invalid input type

Explanation:
InputMismatchException is thrown by Scanner when input does not match expected data type. When user enters character "A" for integer input, exception is thrown. 
Catch this exception and display message about correct input format required.
"""

try:
	num=input("Enter number =")
	num=int(num)
	print("num = ",num)
except ValueError:
	print("Invalid input type")