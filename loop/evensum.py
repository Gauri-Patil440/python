"""Question 7: Write a java program to find the sum of all even numbers between 1 to n.
Asked In Just Practice assignment
Input:

n = 10

Output:

Sum = 30

Explanation:

Even numbers between 1 and 10 are 2, 4, 6, 8, 10.
Their sum is 2 + 4 + 6 + 8 + 10 = 30."""


	  
n = int(input("Enter number: "))
i = 2
sum = 0

while i <= n:
    sum = sum + i
    i += 2

print(sum)