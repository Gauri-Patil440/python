"""Question 52: Write a function that accepts one integer and prints whether the number is Even or Odd.

Description: Use modulo operator %. If number % 2 == 0, print Even. Otherwise, print Odd. No return value used.
Asked In Practice Assignment
INPUT:
Number: 7

OUTPUT:
Number is Odd

EXPLANATION:
The function receives parameter num=7. Check condition: 7 % 2 = 1 (not 0). Since remainder is 1 (not 0), the number is odd. Print "Number is Odd". 
Method signature: void checkEvenOdd(int num) 
                  { 
				      if(num%2==0) 
					  System.out.println("Number is Even"); 
					  else 
					  System.out.println("Number is Odd"); 
				  }"""
				  


				  
def EvenOdd(n):
  if n % 2 == 0:
     print("Number is Even")
  else:
     print("Number is Odd")
n=int(input("Enter Number"))
EvenOdd(n)