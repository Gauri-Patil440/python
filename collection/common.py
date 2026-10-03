"""Question 15: Write a java program to find common elements between two arrays.
Asked In Practice assignment
Input :
Array1 = {1, 2, 3, 4, 5}
Array2 = {3, 4, 5, 6, 7}
Output : Common elements = {3, 4, 5}
Explanation :
Compare each element of Array1 with all elements of Array2, if match found ? it is a common element."""

n1 = int(input("Enter size of first array = "))
arr1 = input("Enter first array elements = ").split()

n2 = int(input("Enter size of second array = "))
arr2 = input("Enter second array elements = ").split()

print("common element=")

for i in range(n1):
    for j in range(n2):
	   
	    if arr1[i]==arr2[j]:
		    print(arr1[i],end=" ")