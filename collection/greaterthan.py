"""Question 20: Write a Java program to print all elements from an integer array that are greater than a given number.
Asked In Practice assignment
Input:
Array = [10, 25, 5, 40, 18]
Given Number = 20

Output:
Elements greater than 20: 25 40

Explanation:
Traverse the array and compare each element with the given number; if the element is greater than the number, print it."""



n = int(input("Enter array size = "))

arr = input("Enter array elements = ").split()

number = int(input("Enter given number = "))

print("Elements greater than", number, "=", end=" ")

for i in range(n):
    num = int(arr[i])

    if num > number:
        print(num, end=" ")