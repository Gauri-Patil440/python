"""Question 23: Write a Java program to find the Majority Element of an array.
A majority element in an array of size n is an element that appears more than n/2 times. There can be at most one majority element in the array.
Asked In Practice assignment
Input:
Array = [4, 8, 4, 6, 7, 4, 4, 8]

Output:
Majority Element = 4

Explanation:
Count the occurrences of every element using nested traversal and if any element appears more than n/2 times it is the majority element."""


"""n=int(input("Enter array size = "))

arr=input("Enter array element = ").split()

majority = -1

for i in range(n):
  count=0

  for j in range(n):
    if arr[i] == arr[j]:
	    count=count + 1
		
    if count > n / 2:
	   majority = arr[i]
	   break
	
if majority != -1:
    print("majority element =", majority)
else:
    print("no majority element ")"""
    
    
n = int(input("Enter array size = "))

arr = input("Enter array element = ").split()

majority = -1

for i in range(n):
    count = 0

    for j in range(n):
        if arr[i] == arr[j]:
            count = count + 1

    if count > n / 2:
        majority = arr[i]
        break

if majority != -1:
    print("Majority element =", majority)
else:
    print("No majority element")