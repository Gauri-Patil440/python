"""2.Find the Maximum Element
Write a Python program to create a set of integers and find the largest element in the set."""


a={10,20,30,40,50}

maximum = 0
for i in a:
   if i > maximum:
      maximum = i
   
print("maximum = ", a)
print("largest element in set = ",maximum)