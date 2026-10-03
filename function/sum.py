"""Question 51: Write a function that accepts two integers and prints their sum.

Description: Function takes two numbers as parameters. Calculates sum inside the function. Prints the result. No return type needed.
Asked In Practice Assignment
INPUT:
First Number: 10
Second Number: 20

OUTPUT:
Sum = 30

EXPLANATION:
The function receives two integer parameters a=10 and b=20. Inside function, sum = a + b = 10 + 20 = 30. The result is printed directly using System.out.println(). 
In Java, method signature would be: void addNumbers(int a, int b) { System.out.println("Sum = " + (a+b)); }"""



def add(a,b):
   sum=a+b
   return sum
result = add(10,20)
print(result)   
