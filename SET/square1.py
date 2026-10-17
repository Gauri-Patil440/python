"""6.Find the Square of Each Element
Write a Python program to create a set of integers and create a new set containing the square of each
element."""

"""n=int(input("enter number of element"))

square = set()

for i in a:
	x=int(input("enter element"))
    x = i * i
    square = square | {x}

print("Original set =", a)
print("Square set =", square)"""


n = int(input("Enter number of elements: "))

a = set()

for i in range(n):
    x = int(input("Enter element: "))
    a.add(x)

square = set()

for i in a:
    x = i * i
    square.add(x)

print("Original set =", a)
print("Square set =", square)