"""Question 8: Write a java program to find the sum of all odd numbers between
Asked In Just Practice assignment
Input:

n = 10

Output:

Sum = 25

Explanation:

Odd numbers between 1 and 10 are 1, 3, 5, 7, 9.
Their sum is 1 + 3 + 5 + 7 + 9 = 25."""


n=int(input("Enter number="))

i=1
sum=0

while i<=n:
   sum=sum+i
   i+=2
   
print(sum)