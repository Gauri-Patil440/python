"""Question 20: Write a Java program to compute the sum of digits of an integer.
Asked In Basic program
Input:
123

Output:
6

Explanation:
Each digit is separated using modulus and division operations.
1 + 2 + 3 = 6."""

num = int(input("Enter number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num / 10

print("Sum of digits =", sum)