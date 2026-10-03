"""Question 5: Write a Java program to count even & odd values from an array.
Asked In Practice assignment
Input:
Array Size = 7
Array Elements = 12 17 24 39 40 55 70
Output:
Count of Even Values = 4
Count of Odd Values = 3
Explanation:
? Initialize counters: evenCount = 0, oddCount = 0.
? For each element in the array:

? If divisible by 2 ? increase evenCount.
? Otherwise ? increase oddCount.

? Final counts are displayed.

lightbulb Take a Help"""



n=int(input("Enter array size= "))

arr=list(map(int,input("Enter Array Elements= ").split()))

evencount=0
oddcount=0

for num in arr:
  if num % 2==0:
     evencount=evencount+1
  else:
     oddcount=oddcount+1
print("count of even values= ",evencount)
print("count of odd values= ",oddcount)