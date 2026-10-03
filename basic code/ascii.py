"""Question 16: Write a Java program to print the ASCII value of a given character
Asked In Basic program
Input:
Character = A

Output:
ASCII value = 65

Explanation:
Every character has a unique ASCII value. When a character is typecast to an integer, its ASCII value is obtained. The ASCII value of 'A' is 6"""


#ch = 'A'
#print("ASCIIVALUE=",ord(ch))

ch='A'
for i in range(0,128):
    if chr(i)==ch:
        print("ASCII value=",i)
        break