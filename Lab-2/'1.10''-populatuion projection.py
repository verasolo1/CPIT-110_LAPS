'''
(population projection) The US Census Bureau projects population based on the following assumptions:
One birth every '7' seconds
One death every '13' seconds
One new immigrant every '45' seconds
-
write a program that display the populatuion for each of the next five years.
assuming that current population is '312032486' and one year has '365' days
'''
print('first year :', 312032486 + 365*24*60*60/7 - 365*24*60*60/13 + 365*24*60*60/45)
print('second year :', 2*312032486 + 365*24*60*60/7 - 365*24*60*60/13 + 365*24*60*60/45)
print('third year :', 3*312032486 + 365*24*60*60/7 - 365*24*60*60/13 + 365*24*60*60/45)
print('fourth year :', 4*312032486 + 365*24*60*60/7 - 365*24*60*60/13 + 365*24*60*60/45)
print('fifth year :', 5*312032486 + 365*24*60*60/7 - 365*24*60*60/13 + 365*24*60*60/45)