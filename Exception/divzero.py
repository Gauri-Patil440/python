"""Q1. Division of Two Numbers
Write a Python program to divide two numbers. Handle the exception that occurs when the denominator is zero."""

try:
    a=int(input("Enter number 1 = "))
    b=int(input("Enter number 2 = "))
    result = a / b
    print("result =",result)
    
except ZeroDivisionError:
    print("can not be divide")