'''
Activity 1 (problem 1)
----
Write a program that reads an unspecified number of integers, determines how many
positive and negative values have been read, and computes the total and average of the
input values (not counting zeros). Your program ends with the input 0. Display the average
as a floating-point number.
'''
Positive = 0
Negative = 0
count = 0
total = 0
number = eval(input('Enter an integer, the input ends if it\'s 0 : ' ))
#-
while number != 0:
    if number > 0:
        Positive += 1
    elif number < 0:
        Negative += 1

    total += number
    count += 1
    number = eval(input('Enter the next integer, the input ends if it\'s 0 : '))
if count == 0:
    print('No numbers are entered exepet 0')
else:
    average = total / count
    print("The number of positives is : ", Positive)
    print("The number of Negatives is : ", Negative)
    print("The Total is : ", total)
    print("The average is : ", average)
