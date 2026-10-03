"""Question 56: Write a function to check whether a given two-digit number is a special number.
 A number is special if: (sum of digits + product of digits) = original number.
Description: Pass the number to a function. Extract digits using % and /. Calculate sum and product. 
Print result inside the function.
Asked In Practice Assignment
INPUT:
Number: 19
OUTPUT:
19 is a Special Number
EXPLANATION:
For number 19: First digit = 19/10 = 1. 
               Second digit = 19%10 = 9. 
			   Sum of digits = 1+9 = 10. 
Product of digits = 1*9 = 9. Total = 10+9 = 19. 
Since total equals original number, 19 is special. 
For any non-special number like 20: digits 2,0 -> sum=2, product=0 -> total=2, not 20, so not special. 
Check using: if(sum+product == number) print "Special" else print "Not Special"."""


def digitdisplay(n):
    firstdigit = n // 10
	seconddigit = n % 10
	sumdigit=firstdigit + seconddigit
	product = firstdigit * seconddigit

	if(sum + product == n):
	  print("Special")
	else:
	   print("Not Special")
	   
n=int(input("Enter Number ="))
digitdisplay(n)
