"""Q.8
Simple Login System
Write a Python program to create a ictionary containing usernames and passwords. 
Ask the user to enter a username and password and check whether the login details are correct."""



loginsystem = {}

username = input("Enter the username = ")
password = input("Enter the password = ")

loginsystem[username]=password


search = input("Enter username to search = ")

if search in loginsystem:
	print("login details are correct")
else:
	print("login details are not correct")