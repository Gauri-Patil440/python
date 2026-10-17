"""12.Convert a list into a tuple."""

a=input("enter 1 element =")
b=input("enter 2 element = ")
c=input("enter 3 element = ")
d=input("enter 4 element = ")

t1=[a,b,c,d]
print("list =",t1)

t=(a,b,c,d)
print("tuple =",t)

list=tuple(t)
print(type(t))
