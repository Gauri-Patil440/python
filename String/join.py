"""13. Join a list of words into a single string."""

a = input("Enter words = ")
b = a.split()

print("Split =", b)
print("Join =", " ".join(b))