'''
assume a runner runs 14 kilometers in 45 minutes and 30 seconds.
write a program that displays the average speed in miles per hour.
note:( 1 mile is 1.6 kilometers).
-
The runner speed in km per hour is : 18.46 Kilometers per hour
The runner speed in Mile per hour is : 11.47 Kilometers per hour
11.47 kilo/1.6 = ((7.17 mile))
'''
d1 = float(input('enter distance in Kilometer number 1 :'))
d11 = d1/7.17
d2 = float(input('enter distance in Kilometer number 2 :'))
d22 = d2/7.17
d3 = float(input('enter distance in Kilometer number 3 :'))
d33 = d3/7.17
t1 = float(input('enter time number 1 :'))
t2 = float(input('enter time number 2 :'))
t3 = float(input('enter time number 3 :'))
v1 = d11/t1
v2 = d22/t2
v3 = d33/t3
average = v1+v2+v3/3
print('your average speed in mile per hour :', average , 'mile per hour.')