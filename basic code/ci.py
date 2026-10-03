"""Question 13: Write a Java program to calculate compound interest.
Asked In Basic program
Input:
Principal = 2000
Rate = 10
Time = 2

Output:
Compound Interest = 420

Explanation:
Compound Interest is calculated using the formula:
CI = P(1 + R/100)^T ? P
After calculation, the compound interest is 420."""


Principal = 2000
Rate = 10
Time = 2

amount = Principal
year = 1

while year <= Time:
    interest = amount * Rate / 100
    amount = amount + interest
    year = year + 1
ci = amount - Principal
print("compound Interest=",ci)