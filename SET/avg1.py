"""4. Calculate the Average of Set Elements
Write a Python program to create a set of integers and calculate the average of all elements."""


n=int(input("Enter number of elements ="))

sum=0
count=0

for i in range(n):      
    x=int(input("enter elements ="))
    sum=sum+x
    count=count+1
	
    
print("sum =" ,sum)
avg=sum/count

print("average of all elements = ",avg)

