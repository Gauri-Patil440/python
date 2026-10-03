"""Question 17: Write a Java program to count the number of even and odd elements present in a given integer array.
Asked In Practice assignment
Input :- Array = { 10, 15, 20, 25, 30 }
Output :- Even count = 3
Odd count = 2 Explanation
? An even number is a number that is completely divisible by 2.
? An odd number is a number that is not divisible by 2.
? Traverse the array using a loop."""


"""arr=int(input("Enter array elements= "))

evencount=0
oddcount=0

for num in arr:
    num=int(num)
    
    if num % 2 == 0:
	   evencount = evencount + 1
       
	else:
	   oddcount = oddcount + 1
	   
print("evencount = ",evencount)
print("oddcount = ",oddcount)"""


arr = input("Enter array elements = ").split()

evencount = 0
oddcount = 0

for num in arr:
    num = int(num)

    if num % 2 == 0:
        evencount = evencount + 1
    else:
        oddcount = oddcount + 1

print("evencount =", evencount)
print("oddcount =", oddcount)