"""
activity 3 (problem 3)
The area of a pentagon can be computed using the following formula
(s is the length of a side):
--------
Area = (5 * s ** 2) / (4 * tan(math.pi / 5))
"""
s = eval(input('Enter the side :'))
import math

area = 5 * s **2  / 4 * math.tan(math.pi / 5)
print('The area of the pentagon is', area)
