"""Question 21: Given an integer array and a specific element, write a Java program to find the index position of that element in the array. If the element is not found, print -1.
Asked In Practice assignment
Input:
Array = [10, 20, 30, 40, 50]
Element to find = 30

Output:
Element found at index = 2

Explanation:
Traverse the array from index 0 and compare each element with the target value; when a match is found return its index otherwise return -1 if the element is not present.

lightbulb Take a Help"""

n = int(input("Enter array size = "))

arr=input("Enter array element = ").split()

value=int(input("Enter element of find = "))
index = -1

for i in range(n):
    
  if arr[i] == value:
     index = i
     break
print("Element found at index  = ",index)