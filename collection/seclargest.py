"""Question 11: Write a java program to give an array, find the second largest element.
Asked In Practice assignment
Input : Array = {12, 35, 1, 10, 34, 1}
Output : Second largest = 34
Explanation:
First largest is 35, second largest is the next maximum (34). We maintain two variables (largest, secondLargest)."""


arr=list(map(int,input("Enter array element= ").split()))

largest = arr[0]
secondLargest = arr[0]

for num in arr:
    if num > largest:
	   secondlargest = largest
	   largest = num
       
    elif num > secondlargest and num != largest:
       secondlargest = num
       
print("secondlargest= ",secondlargest)