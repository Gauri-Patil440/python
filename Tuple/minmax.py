"""18.Find the maximum and minimum value in a tuple."""


a = int(input("Enter 1 element = "))
b = int(input("Enter 2 element = "))
c = int(input("Enter 3 element = "))
d = int(input("Enter 4 element = "))
e = int(input("Enter 5 element = "))

t = (a, b, c, d, e)

print("Tuple =", t)
print("Maximum value =", max(t))
print("Minimum value =", min(t))