"""9.Check if an element exists in a tuple."""


a=input("Enter 1 element = ")
b=input("Enter 2 element = ")
c=input("Enter 3 element = ")
d=input("Enter 4 element = ")

t=(a,b,c,d)


num=input("number search= ")
print("tuple = ",t)

if num in t:

    print("Element Exists in tuple")
	
else:

    print("Element not Exists")