"""Q.3
Phone Book
Write a Python program to take a person's name and phone number as input and store them in a dictionary.
Ask the user for a name and display the corresponding phone number."""

phonebook = {}

name = input("Enter person name = ")
phone = int(input("Enter phone number = "))

phonebook[name] = phone

search = input("Enter name to search = ")

if search in phonebook:
    print("Phone number =", phonebook[search])
else:
    print("Name not found")