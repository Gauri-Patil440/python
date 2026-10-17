"""19.Create a tuple of numbers and calculate their sum."""


a = int(input("Enter 1 element = "))
b = int(input("Enter 2 element = "))
c = int(input("Enter 3 element = "))
d = int(input("Enter 4 element = "))
e = int(input("Enter 5 element = "))

t = (a, b, c, d, e)

print("Tuple =", t)
print("Sum =", sum(t))