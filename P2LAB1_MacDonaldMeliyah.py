#Meliyah MacDonald
#6/22/25
#P2Lab1
#Calculating the diameter, circumference, and area of a circle.

import math
radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius * radius

print()
print("The diameter of the circle is", diameter)
print("The circumference of the circle is", round(circumference, 2))
print("The area of the circle is", round(area, 3))
