'''
Activity 1 (Problem 1)
------------------
Write a program that reads in the radius and length of a cylinder and computes the area and volume using the
 following formulas:
---
pi = 3.14159
area = radius * radius * pi
volume = area * length
'''
while True:
 i = 0
 radius = float(input('enter your cylinder radius : '))
 length = float(input('enter your cylinder length : '))
 if radius == i:
     break
 area = radius * radius * 3.14159
 volume = area * length
 print('area = ', area)
 print('volume = ', volume)
