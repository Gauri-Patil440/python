"""Question 18: Write a Java program to check whether a given array is empty or not.
Asked In Practice assignment
Input :- Array elements: { } Explanation
1. Every array has a predefined property called length.
2. If array.length == 0, then the array is empty.
3. Otherwise, the array contains elements.
Output :- Array is empty"""

n=int(input("Enter array size = "))

if n == 0:
   print("array is empty")
else:
   print("array is not empty")