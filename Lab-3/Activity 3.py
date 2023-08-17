'''
Activity 3 (Problem 3)
------------------
Write a program that reads a celsius degree from the console and converts it
to Fahrenheit and displays the result. The Formula for the conversion os as follows:
------
fahrenheit = (9/5) * celsius + 32
'''
while True:
    i = 0
    celsius = eval(input('Enter a degree in celsius : '))
    fahrenheit = (9/5) * celsius + 32
    print(celsius, 'celsius is', fahrenheit, 'with fahrenheit.' )
    if celsius == i:
        break