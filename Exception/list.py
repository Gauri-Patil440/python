"""Q3. List Index Error
Create a list of five numbers. Ask the user to enter an index and display the corresponding element. Handle an invalid index."""


try:
	a=[10, 20, 30, 40, 50]
    i=int(input("Enter index ="))
    print("Element =", a[i])

except IndexError :
    print("invalid Index")
    
except valueError :
    print("Enter valid Index")