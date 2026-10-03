"""Question 53: Write a function that accepts an integer N and prints numbers from 1 to N.

Description: Function receives value of N. Use a loop inside the function. Print numbers one by one.
Asked In Practice Assignment
INPUT:
N: 5

OUTPUT:
1 2 3 4 5

EXPLANATION:
The function receives parameter N=5. Use a for loop from i=1 to i<=N. In each iteration, print i. Loop executes 5 times printing 1, 2, 3, 4, 5 sequentially. 
Method signature: void printNumbers(int N) { 
                   for(int i=1; i<=N; i++) 
				   System.out.print(i+" "); 
				   }"""
				   
				   
				   
def printNumber(n):
    for i in range(1, n + 1):
        print(i, end=" ")
        
n=int(input("Enter Number"))
printNumber(n)
