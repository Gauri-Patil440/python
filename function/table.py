"""Question 55: Write a function that accepts a number and prints its multiplication table up to 10.

Description: Use a loop from 1 to 10. Multiply number with loop variable. Print result inside function.
Asked In Practice Assignment
INPUT:
Number: 3

OUTPUT:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

EXPLANATION:
The function receives num=3. Use for loop from i=1 to i<=10. In each iteration, calculate: result = num * i. 
Print "3 x i = result". Loop runs 10 times generating complete multiplication table. 
Method signature: void printTable(int num) { for(int i=1; i<=10; i++) System.out.println(num+" x "+i+" = "+(num*i)); }"""


def showtable(n):
    for i in range(1,11):
        print(n," x ",i," = ", n*i)
    
    
n = int(input("Enter Number= "))
showtable(n)
 
