#Write a Python program to calculate the area of regular polygon.
from math import tan, radians
n = float(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
p = n*l    #perimeter
rad_to_deg = radians(180/n)
a = l/(2*tan(rad_to_deg))    #apothem
A = p*a/2    #area
print("The area of the polygon is:", A)