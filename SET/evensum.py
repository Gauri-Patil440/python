"""5.Find the Sum of Even Numbers
Write a Python program to create a set of integers and calculate the sum of only the even numbers."""


a={10,20,13,23,99}

sum=0

for i in a:
    if i % 2 == 0:
        sum=sum+i
print("Set =", a)
print("sum of only even numbers = ",sum)
