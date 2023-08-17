'''
activity 1 (problem 1)
Write a program that prompts the user to enter the length from the center of a pentagon
to a vertex and computes the area of the pentagon, as shown in the following figure.
----
The formula for computing the area of a pentagon is...
area = ( 3 * math.sqrt(3) / 2 ) * s ** 2
----
The side can be computed using the formula...
s = 2r * sin * (math.pi / 5)
'''
import math
r = eval(input('Enter the length from the center to a vertex : '))

s = 2 * r * math.sin(math.pi / 5)

area = (3 * math.sqrt(3) / 2) * s ** 2

print('The area of the pentagon is ', area)