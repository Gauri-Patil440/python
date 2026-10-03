"""Question 19: Given an integer array, replace all the negative numbers in the array with 0 and print the updated array.
Asked In Practice assignment
Input:
Array = [5, -3, 7, -1, 0, -6, 4]

Output:
Updated Array = [5, 0, 7, 0, 0, 0, 4]

Explanation:
Traverse the array and check each element; if the element is negative replace it with 0, otherwise keep it unchanged, then print the modified array."""

n = int(input("Enter array size = "))

arr = input("Enter array elements = ").split()

for i in range(n):

    num = int(arr[i])

    if num < 0:
        arr[i] = 0

print("Replace numbers =", arr)