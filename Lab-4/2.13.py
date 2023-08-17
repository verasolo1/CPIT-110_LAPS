'''
(Split digits)
2.13 - page 78
---
write a program that prompts the user to enter a for-digit integer
and displays the number in reverse order.
'''
i = 0
x = int(input('enter an integer : '))

list = list(map(int, str(x)))

print(list)


