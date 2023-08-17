"""
programming exercises: 4.12 - Page 142
---
Write a program that prompts the user to enter an integer and
checks whether the number is divisible by both 5 and 6, divisible by 5 or 6, or just
one of them (but not both).
"""
while True:
    number = eval(input('enter a number : '))
    if number % 5 == 0:
        print(number, 'is divisible on 5')
    elif number % 6 == 0:
        print(number, 'is divisible on 6')
    else:
        print("can't be divisible on both")
