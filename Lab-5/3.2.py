'''
(ComputeAngels.py)
3.2 - page 86
'''
import math

x1, y1, x2, y2, x3, y3 = eval(input('enter three points : '))

c = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
b = math.sqrt((x1 - x3) * (x1 - x3) + (y1 - y3) * (y1 - y3))
a = math.sqrt((x2 - x3) * (x2 - x3) + (y2 - y3) * (y2 - y3))

A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * b * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

print('The three angles are', round(A * 100) / 100)
print(round(B * 100) / 100, round(C * 100) / 100)