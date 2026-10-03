"""Question 19: Write a java program to find the sum of the first and last digit of a number.
Asked In Just Practice assignment
Input:

Number = 1234

Output:

Sum = 5

Explanation:

First digit = 1
Last digit = 4
Sum = 1 + 4 = 5."""


n=int(input("Enter number= "))
sum=0
last = n % 10
while n >= 10:
    n = n // 10
first = n
sum=first + last
print(sum)