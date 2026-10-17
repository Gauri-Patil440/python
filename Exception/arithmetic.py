"""Question 5: Write a Java program to demonstrate multiple catch blocks.

Accept two numbers and perform division and also store the result in an array. 
Handle both ArithmeticException and ArrayIndexOutOfBoundsException separately.
Asked In Practice Assignment
Input:
Enter number1: 20
Enter number2: 0

Output:
Arithmetic Exception handled

Explanation:
Multiple catch blocks allow handling different exception types differently. 
First catch block handles ArithmeticException for division by zero. 
Second catch block handles ArrayIndexOutOfBoundsException for invalid array access. 
Each block provides specific error handling for its exception type."""

"""
try:
	a= int(input("Enter first number1 = "))
	b= int(input("Enter first number2 = "))
    result = a/b
	arr=[result]    
    index = int(input("Enter index ="))
    print("Result =",arr[index])
        	
except ZeroDivisionError:
    print("Arithmetic Exception Handle")

except IndexError:
	print("Array Index Out Of Bounds Exception handled")"""
    
    
    
try:
    a = int(input("Enter first number1 = "))
    b = int(input("Enter first number2 = "))

    result = a / b

    arr = [result]

    index = int(input("Enter index = "))

    print("Result =", arr[index])

except ZeroDivisionError:
    print("Arithmetic Exception handled")

except IndexError:
    print("Array Index Out Of Bounds Exception handled")