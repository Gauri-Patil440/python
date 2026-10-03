"""Question 10: Write a program in java to delete an element at desired position from an array.
Asked In Practice assignment
Input the size of array : 5

Input 5 elements in the array in ascending order :
1 2 3 4 5

Input the position where to delete : 3

Expected Output : The new list is : 1 2 3 5"""


n=int(input("enter array size= "))
arr=list(map(int,input("Enter array element= ").split()))

print("before remove= ",arr)
value=int(input("enter remove value= "))
arr.remove(value)
print("after remove=",arr)