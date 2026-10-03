"""Question 54: Write a function that accepts two integers and prints the greater number.

Description: Compare both numbers using if-else. Print the greater number. Function does not return anything.
Asked In Practice Assignment
INPUT:
Number 1: 15
Number 2: 25

OUTPUT:
Maximum number is 25

EXPLANATION:
The function receives a=15 and b=25. Compare using if condition: if(a > b) then a is greater, else b is greater. Here 15 > 25 is false, so b (25) is the greater number. Print "Maximum number is 25". 
Method signature: void findGreater(int a, int b) { if(a>b) System.out.println(a); else System.out.println(b); }"""



def findGreater(num1,num2):
  if num1 > num2:
     print("maximum number is =",num1)
  else:
     print("maximum number is =",num2)

num1 = int(input("Number 1= "))
num2 = int(input("Number 2= "))

findGreater(num1,num2)