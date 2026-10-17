"""16.Iterate through a tuple using a while loop."""



a=input("Enter 1 element = ")
b=input("Enter 2 element = ")
c=input("Enter 3 element = ")
d=input("Enter 4 element = ")

t=(a,b,c,d)

print("tuple = ",t)

i = 0

while i < len(t):
    print(t[i])
    i += 1