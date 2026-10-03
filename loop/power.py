"""Question 16: Write a java program to find power of a number.
Asked In Just Practice assignment
Input:

Base = 2
Exponent = 3

Output:

Result = 8

Explanation:

2 raised to the power 3 means 2 * 2 * 2.
The result is 8."""


base = int(input("Base= "))
power = int(input("Power= "))

ans = 1

while power > 0:
    ans = ans * base
    power -= 1

print(ans)
