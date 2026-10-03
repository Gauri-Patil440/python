"""Question 17: Write a java program to find all factors of a number.
Asked In Just Practice assignment
Input:

Number = 12

Output:

Factors: 1 2 3 4 6 12

Explanation:

A factor divides the number completely without remainder.
All numbers that divide 12 exactly are printed."""


n = int(input("Enter number= "))
i = 1

while i <= n:
    if n % i == 0:
        print(i)
    i += 1

