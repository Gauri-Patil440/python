"""Question 10: Write a Java program to demonstrate nested try blocks.

Create nested try blocks where the inner block handles ArithmeticException and outer handles ArrayIndexOutOfBoundsException.
Asked In Practice Assignment
Input:
Enter number: 10
Enter divisor: 0

Output:
Inner exception handled

Explanation:
Nested try blocks allow handling different exceptions at different levels. 
Inner try block catches ArithmeticException when divisor is zero. Outer try block can catch ArrayIndexOutOfBoundsException if it occurs. 
This hierarchical exception handling provides fine-grained control."""


try:
	a=int(input("Enter number = "))
	b=int(input("Enter divisor = "))
	
	try:
		result = a/b
		print("result =",result)
		
	except ZeroDivisionError:
		print("Inner exception handled")
		
except IndexError:
	print("outer exception handled")