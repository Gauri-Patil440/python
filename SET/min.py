"""3. Find the Minimum Element
Write a Python program to create a set of integers and find the smallest element in the set."""


a={10,20,30,40,50}
minimum = 50
#minimum = maximum

for i in a:
   if i < minimum:
      minimum = i
      
print("minimum ",a)
print("smallest element in set = ",minimum)