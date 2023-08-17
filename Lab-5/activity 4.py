'''
activity 4 (problem 4)
Write a program that prompts the user to enter a four-digit integer and displays the
number in reverse order.
'''

numbers = int(input("enter an integer : "))
reverse = 0
while(numbers>0):
    x = numbers % 10
    reverse = reverse * 10 + x
    numbers = numbers // 10
print("the reversed number is",reverse)
