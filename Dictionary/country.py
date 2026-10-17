"""Q.7
Display the dictionary.
Country and Capital
Write a Python program to take the names of three countries and their capitals from the user and store them in a dictionary. 
Display all country-capital pairs."""

country = {}

for i in range(3):
    name = input("Enter country name = ")
    capital = input("Enter capital name = ")

    country[name] = capital

print("Country and Capital:")

for name in country:
    print("Country = ", name)
    print("Capital = ", country[name])