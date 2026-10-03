"""Question 14: Write a java program to remove duplicated values from arrays.
Asked In Practice assignment
Input : Array = {10, 20, 20, 30, 40, 40, 50}
Output : Unique elements = {10, 20, 30, 40, 50}
Explanation:
Traverse the array, check if element already exists before adding to result, thus avoiding duplicates."""



n = int(input("Enter array size = "))

arr = input("Enter array elements = ").split()

print("duplicated elements = ",end = " ")

for i in range(n):
    count=0
    
    for j in range(n):
        
        if arr[i]==arr[j]:
            count=count+1
            
    if count > 1:
	   print(arr[i],end=" ")