"""Question 16: Write a Java program to calculate the average of all elements present in an integer array.
Asked In Practice assignment
Input Array:
[10, 20, 30, 40, 50]
Output:
Average of array elements = 30Explanation
? The average of array elements is calculated by:
Average=Sum of all elementsNumber of elements\text{Average} = \frac{\text{Sum of all elements}}{\text{Number of elements}}Average=Number of elementsSum of all elements
? First, iterate through the array and add all elements to a variable sum.
? Then divide sum by the total number of elements (array.length) to get the average."""



n = int(input("Enter array size = "))

arr = input("Enter array elements = ").split()

total = 0
count = 0

for i in range(n):
    num = int(arr[i])
    total = total + num
    count = count + 1

average = total / count

print("Average =", average)