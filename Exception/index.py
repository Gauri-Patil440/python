"""Question 2: Write a Java program to handle ArrayIndexOutOfBoundsException while accessing array elements.

Create an integer array of fixed size and allow the user to enter an index number. If the index is beyond array size, 
handle the exception properly.
Asked In Practice Assignment
Input:
Enter array size: 5
Enter index to access: 7

Output:
Exception occurred: Index is out of range

Explanation:
ArrayIndexOutOfBoundsException occurs when accessing array index that does not exist. 
If user enters index 7 but array size is 5 (valid indices 0-4), exception is thrown. 
Catch this exception and display user-friendly message about valid range."""

"""

try:

	size = int(input("Enter array size = "))
    #arr = []
    
    for i in range(size)
        arr.append(i)
        
	index= int(input("Enter index of access = "))
 
    print("Element =", arr[index])

except ArrayIndexOutOfBoundsException:
	
	print("Index is out of range")""" 
    
    
    
    
    
try:

    arr = [10, 20, 30, 40, 50]

    size = int(input("Enter array size = "))

    index = int(input("Enter index to access = "))

    print("Element =", arr[index])

except IndexError:

    print("Index is out of range")