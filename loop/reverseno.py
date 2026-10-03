"""Question 13: Write a java program to enter a number and print its reverse.
Asked In Just Practice assignment
Input:

Number = 1234

Output:

Reversed Number = 4321

Explanation:

The program extracts the last digit and builds the reverse number.
Each digit is added in reverse order."""


n=int(input("Enter number"))

rev=0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

print(rev)
