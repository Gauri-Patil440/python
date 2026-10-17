"""4. Calculate the Average of Set Elements
Write a Python program to create a set of integers and calculate the average of all elements."""


a={10,20,30,40,50}

sum=0
count=0

for i in a:
   sum=sum+i
   count=count+1
   
print("sum = ",a)

avg=sum/count

print("average of all elements = ",avg)