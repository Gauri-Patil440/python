"""Question 12: Write a program in java to insert an element at desired position from an array.
Asked In Practice assignment
Input the size of array : 6

Input 5 elements in the array in ascending order :
1 2 3 4 5

Input the position where to insert : 2
Value : 200

Expected Output : The new list is : 1 2 200 3 4 5"""

n=int(input("enter array size= "))

arr=list(map(int,input("Enter array element= ").split()))
print("before insert= ",arr)
index = int(input("Enter position = "))
value=int(input("enter insert value= "))
arr.insert(index,value)

print("after insert= ",arr)