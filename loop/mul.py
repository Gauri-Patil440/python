"""Question 12: Write a java program to calculate the product of digits in a number.
Asked In Just Practice assignment
Input:

Number = 1234

Output:

Product of digits = 24

Explanation:

Digits are extracted one by one.
1 * 2 * 3 * 4 = 24."""


n=int(input("Enter number"))
mul=1

while n > 0:
    mul= mul*(n % 10)
    n = n // 10
print(mul)