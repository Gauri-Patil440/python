"""Question 8: Write a java program to find missing elements in an array.
Asked In Practice assignment
Input : Array = {1, 2, 4, 5, 7} (numbers from 1 to 7 should be present)
Output : Missing elements = {3, 6}
Explanation:
Check sequence numbers one by one. If a number from 1 to maximum (7) is not in the array, it is missing."""


n=int(input("Enter array size= "))

arr=list(map(int,input("Enter array elements= ").split()))

for num in range(1,n+1):
   if num not in arr:
      print("Missing numbers= ",num)
	  
    