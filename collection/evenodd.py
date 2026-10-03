"""Question 3: Write a Java program to display even & odd values from an array.
Asked In Practice assignment
Input:
Array Size = 6
Array Elements = 11 20 33 42 55 60
Output:
Even Values = 20 42 60
Odd Values = 11 33 55
Explanation:
? Traverse the array element by element.
? If an element is divisible by 2, it is even. Otherwise, it is odd.
? Separate lists are displayed for even and odd values."""



n=int(input("Enter the array size ="))

arr=list(map(int,input("Enter Elements= ").split()))

even=[]
odd=[]
for num in arr:
  if num % 2==0:
    even.append(num)
  else:
    odd.append(num)
      
      
print("Even num= ",even)
print("odd num= ",odd)