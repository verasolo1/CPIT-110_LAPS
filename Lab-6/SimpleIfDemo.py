"""
programming exercises: 4.2 - Page 116
---
"""
while True:
    i = 0
    number = eval(input('enter an integer : '))

    if number % 5 == 0:
        print('HiFive')

    if number % 2 == 0:
        print('HiEven')
        if number == i:
            break
