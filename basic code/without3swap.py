"""Question 15: Write a Java program to swap two numbers without using a third variable.
Asked In Basic program
Input:
A = 4
B = 7

Output:
A = 7
B = 4

Explanation:
Swapping is done using arithmetic operations such as addition and subtraction without using an extra variable."""


A = 4
B = 7

print("Before swaping=")
print("A=",A)
print("B=",B)

A=A+B
B=A-B
A=A-B

print("After swaping=")
print("A=",A)
print("B=",B)