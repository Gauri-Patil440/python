"""Q4. Multiple Exceptions
Write a Python program to accept two numbers and divide them. Handle both ValueError and ZeroDivisionError."""

try:
    a = int(input("Enter first number = "))
    b = int(input("Enter second number = "))

    print("Answer =", a / b)

except ValueError:
    print("enter valid integer values")

except ZeroDivisionError:
    print("Cannot divide by zero")