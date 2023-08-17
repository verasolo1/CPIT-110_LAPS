'''
2.14 - page 78
(Geometry: area of a triangle) write a program that prompts the user to enter the
three points (x1,y1),(x2,y2), and (x3,y3) of a triangle and displays its area.
the formula for computing the area of a triangle is
--------
s = (side1 + side2 + side3) / 2
-
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
'''
import math
side1 = eval(input('enter side number one : '))
side2 = eval(input('enter side number two : '))
side3 = eval(input('enter side number three : '))

s = (side1 + side2 + side3) / 2

area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print('the area of the triangle is ', area)


