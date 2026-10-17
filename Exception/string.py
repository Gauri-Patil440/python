"""Question 3: Write a Java program to handle NumberFormatException while converting string into integer.

Accept a number in string format from the user and convert it into integer using parsing. If the input is not numeric, 
handle the exception.
Asked In Practice Assignment
Input:
Enter number: ABC

Output:
Invalid number format

Explanation:
NumberFormatException is thrown when Integer.parseInt() or similar methods receive non-numeric string input. 
When user enters 'ABC' instead of a number, parsing fails because alphabetic characters cannot be converted to integers. Catch NumberFormatException and display message that input must be numeric.
 This exception handling prevents program crash and provides user feedback."""
 
"""
try:
    number=input("Enter numbers = ")
    num = int(number)
    print("Number =",number)

except TypeError as e:
    print(e)"""
    
try:

    number = input("Enter number: ")

    number = int(number)

    print("Number =", number)

except ValueError:

    print("Invalid number format")