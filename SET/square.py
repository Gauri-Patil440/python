"""6.Find the Square of Each Element
Write a Python program to create a set of integers and create a new set containing the square of each
element."""


a = {10, 20, 30, 40, 50}

square = set()

for i in a:
    x = i * i
    square = square | {x}

print("Original set =", a)
print("Square set =", square)