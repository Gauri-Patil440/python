"""3. Find the Minimum Element
Write a Python program to create a set of integers and find the smallest element in the set."""



n=int(input("Enter number of element = " ))

for i in range(n):
    x=int(input("enter the element = "))
	
    if i == 0:
	    minimum = x
	elif x < minimum:
	    minimum = x

print("smallest element in set = ",minimum)

