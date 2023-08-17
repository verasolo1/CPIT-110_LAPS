'''
Activity 4 (Problem 4)
------------------
Wtite a program that calculates the energy needed to heat water from an
initial temperature to a final temperature. Your program should prompt
the user to enter the amount of water in kilograms and the initial and
final temperatures of the water. The formula to compute the energy is:
-------
formula :
Q = M * (finalTemperature - initialTemperature) * 4184
--------
where 'M' is the 'weight' of water in kilograms, temperatures are in degrees Celsius, and
energy 'Q' is measured in 'joules'.
'''
M = eval(input('Enter the weight in Kilograms "M" : '))
Ti = eval(input('Enter initial Temperature in celsius "Ti" : '))
Tf = eval(input('Enter final Temperature in celsius "Tf" : '))
Q = M * (Tf - Ti) * 4184
print('Q = M * (final Temperature - initial Temperature) * 4184')
print('Q = ', M, '*', '(',Tf ,'-', Ti,')', '*', '4184' )
print('The Energy Needed =', Q)