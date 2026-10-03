"""Question 20: Write a java program to swap first and last digits of a number.
Asked In Just Practice assignment
Input:

Number = 1234

Output:

Swapped Number = 4231

Explanation:

First digit (1) and last digit (4) are interchanged.
Middle digits remain the same."""


n=int(input("Enter number ="))

last = n % 10
first = n

while first >= 10:
    first = first // 10

    middle = (n % 1000) // 10

    result = last * 1000 + middle * 10 + first

print("Swapped Number =", result)
