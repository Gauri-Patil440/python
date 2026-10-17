"""Question 6: Write a Java program to demonstrate finally block execution.

Perform division of two numbers and display result. Whether an exception occurs or not, the finally block must execute.
Asked In Practice Assignment
Input:
Enter number1: 15
Enter number2: 3

Output:
Result is: 5
Finally block executed

Explanation:
Finally block always executes regardless of whether exception occurred or not. It is used for cleanup operations like closing files or 
connections. 
In this case, finally block executes after division is performed and result is displayed."""



try:
	a=int(input("Enter number1 = "))
	b=int(input("Enter number2 = "))
	
	result=a/b
	print("result = ",result)

except:
    print("Exception occurred")
finally:    
	print("finally block executed")
	