"""10.Concatenate two tuples."""


a=input("Enter 1 element = ")
b=input("Enter 2 element = ")
c=input("Enter 3 element = ")
d=input("Enter 4 element = ")

t=(a,b,c,d)

print("tuple = ",t)


f=input("Enter 1 element = ")
g=input("Enter 2 element = ")
e=input("Enter 3 element = ")
h=input("Enter 4 element = ")

t1=(f,g,e,h)

print("tuple = ",t1)

t2=t+t1

print("concatenate = ",t2)