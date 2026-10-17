"""7.Count how many times a specific value appears in a tuple."""



a=input("Enter 1 element = ")
b=input("Enter 2 element = ")
c=input("Enter 3 element = ")
d=input("Enter 4 element = ")
e=input("Enter 5 element = ")
f=input("Enter 6 element = ")

t=(a,b,c,d,e,f)
num=input("number of count = ")
print("tuple = ",t)
print("count = ",t.count(num))