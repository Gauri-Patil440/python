"""Question 5: Write a Java program to enter the radius of a circle and calculate its diameter, area, and circumference.
Asked In Basic program
Input:
Radius = 7

Output:
Diameter = 14
Area = 153.86
Circumference = 43.96

Explanation:
Diameter = 2 * radius
Area = ? * r^2
Circumference = 2 * ? * r
The formulas are applied using the given radius."""

import math
Radius=7

Diameter=2*Radius
Area=math.pi*Radius*Radius
Circumference=2*math.pi*Radius

print("Diameter=",Diameter)
print("Area=",Area)
print("Circumference=",Circumference)