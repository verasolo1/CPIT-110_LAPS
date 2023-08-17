'''
programming exercises: 4.5 - Page 124
---
'''
year = eval(input('enter a year : '))
zodiacyear = year % 12
if zodiacyear == 0:
    print('monkey')
elif zodiacyear == 1:
    print('roster')
elif zodiacyear == 2:
    print('dog')
elif zodiacyear == 3:
    print('pig')
elif zodiacyear == 4:
    print('rat')
elif zodiacyear == 5:
    print('ox')
elif zodiacyear == 6:
    print('tiger')
elif zodiacyear == 7:
    print('rabbit')
elif zodiacyear == 8:
    print('dragon')
elif zodiacyear == 9:
    print('snake')
elif zodiacyear == 10:
    print('horse')
else:
    print('sheep')
