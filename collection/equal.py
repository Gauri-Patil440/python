"""Question 22: Write a Java program to check whether two integer arrays are equal.
Two arrays are considered equal if:
Asked In Practice assignment
Input:
Array1 = [10, 20, 30, 40]
Array2 = [10, 20, 30, 40]

Output:
Arrays are equal.

Explanation:
First compare the lengths of both arrays and if they are equal then compare elements at each index; if all elements match the arrays are equal otherwise they are not."""



n1 = int(input("Enter first array size = "))
arr1 = input("Enter first array elements = ").split()

n2 = int(input("Enter second array size = "))
arr2 = input("Enter second array elements = ").split()

equal = True

if n1 != n2:
    equal = False
else:
    for i in range(n1):
        if arr1[i] != arr2[i]:
            equal = False
            break

if equal == True:
    print("Arrays are equal.")
else:
    print("Arrays are not equal.")