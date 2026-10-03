"""Question 7: Write a java program to display the reverse array.
Asked In Practice assignment
Input : Array = {1, 2, 3, 4, 5}
Output : Reverse array = {5, 4, 3, 2, 1}
Explanation :
The last element becomes the first, and the first becomes the last by traversing from the end to the start."""


arr=list(map(int,input("Enter array element= ").split()))

print("arr before reverse=",arr)
l=0
r=(len(arr)-1)
while l < r:
   temp=arr[l]
   arr[l]=arr[r]
   arr[r]=temp
   l=l+1
   r=r-1
print("arr after reverse =",arr)