"""Question 8: Write a Java program to demonstrate try-catch without exception.

Write code inside a try block which does not generate exceptions and show program flow.
Asked In Practice Assignment
Input:
Enter number: 5

Output:
Number is: 5
Program executed successfully

Explanation:
Try block executes successfully when no exception occurs. The code runs normally and completes execution. 
This demonstrates that try-catch is not only for error conditions but also validates code execution flow. 
Finally block executes after successful try block completion."""



try:
	num=input("Enter Number = ")
	print("num = ",num)

finally:
    print("Program executed successfully")