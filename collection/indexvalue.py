"""Question 4: Write a Java program to display even & odd index values from an array.
Asked In Practice assignment
Input:
Array Size = 6
Array Elements = 5 10 15 20 25 30
Output:
Values at Even Index = 5 15 25
Values at Odd Index = 10 20 30
Explanation:
? Index starts from 0.
? Even index positions are 0, 2, 4, ….
? Odd index positions are 1, 3, 5, ….
? We print the values according to their index category."""


n=int(input("Enter array size= "))

arr=list(map(int,input("Enter Array element =").split()))

even=[]
odd=[]

for num in range(n):
   if num % 2==0:
       even.append(arr[num])
   else:
       odd.append(arr[num])

print("even Index value= ",even)
print("odd Index value= ",odd)