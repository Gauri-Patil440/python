"""8.Find the index of a given element in a tuple."""


a=input("Enter 1 element = ")
b=input("Enter 2 element = ")
c=input("Enter 3 element = ")
d=input("Enter 4 element = ")

t=(a,b,c,d)

num=input("number of index = ")
print("tuple = ",t)

if num in t:

    print("Index =", t.index(num))
	
else:

    print("Element not found")