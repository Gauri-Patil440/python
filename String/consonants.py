"""5. Count the number of consonants in a string."""


s = input("Enter string = ")
c = 0

for i in s:
    if i not in "aeiouAEIOU ":
        c = c + 1

print("Consonants =", c)
print("consonants = ",s)