"""5.Find the Sum of Even Numbers
Write a Python program to create a set of integers and calculate the sum of only the even numbers."""


n=int(input("Enter numbers of elements = "))

sum=0

for i in range(n):
	x=int(input("Enter elements = "))
    
	if x % 2==0:
		sum=sum+x
print("sum of only even numbers = ",sum)