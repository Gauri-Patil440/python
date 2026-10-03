"""Question 14: Write a java program to check whether a number is palindrome or not.
Asked In Just Practice assignment
Input:

Number = 121

Output:

Palindrome

Explanation:

The reversed number of 121 is also 121.
Since original and reversed numbers are equal, it is a palindrome."""

n = int(input("Enter number"))
temp = n
rev = 0

while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
