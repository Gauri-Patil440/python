"""13.Convert a tuple into a list."""


a=input("enter 1 element =")
b=input("enter 2 element = ")
c=input("enter 3 element = ")
d=input("enter 4 element = ")


t=(a,b,c,d)
print("tuple =",t)

t1=[a,b,c,d]
print("list =",t1)

tuple=list(t1)
print(type(t1))

