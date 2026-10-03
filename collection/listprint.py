"""Question 1: Write a Java program to input an array & display it.
Asked In Practice assignment
Input:
Array Size = 5
Array Elements = 10 20 30 40 50
Output:
10 20 30 40 50
Explanation:
? First, we take the size of the array from the user.
? Then, elements are entered one by one into the array.
? Finally, using a loop, we display all elements in the same order they were entered."""


n=int(input("Enter Array size= "))

arr=[]

for i in range(n):
    arr = list(map(int, input("Enter Array Element= ").split()))
   # x=int(input("Enter Array Element= "))
    arr.append(arr)                           
    
print("Array elements are= ")
    
for x in arr:
    print(x, end=" ")                      
