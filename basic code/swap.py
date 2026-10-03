"""Question 14: Write a Java program to swap two numbers using a third variable.
Asked In Basic program
Input:
A = 5
B = 10

Output:
A = 10
B = 5

Explanation:
A temporary variable is used to store one value while swapping the numbers."""


A=5
B=10

print("Before swaping=")
print("A=",A)
print("B=",B)

temp=A
A=B
B=temp

print("After swapping=")
print("A=",A)
print("B=",B)