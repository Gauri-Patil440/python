"""Question 13: Write a java program to display only non-zero values from an array.
Asked In Practice assignment
Input : Array = {1, 0, 5, 0, 7, 0, 9}
Output : Non-zero elements = {1, 5, 7, 9}
Explanation :
Traverse the array and print only elements that are not equal to zero."""



n=int(input("Enter arry size= "))
arr= input("Enter array elements= ").split()
print("non zero elements= ",end=" ")

for i in range(n):
   num = int(arr[i])
   
   if num !=0:
     print(num,end=" ")