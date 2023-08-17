"""
Activity 3 (Problem 3)
-----
Write a program that prompts the user to enter the number of students and each
student’s score, and displays the highest and second highest scores.
"""
students = eval(input('Enter the number of students: '))

name = input('Enter a student name: ')
score = eval(input('Enter a student score: '))

name1, score1 = name, score

name = input('Enter a student name: ')
score = eval(input('Enter a student score: '))

score2, name2 = score, name

if score2 > score1:
    score1, score2 = score2, score1
    name1, name2 = name2, name1

for i in range(students - 2):
    name = input('Enter a student name: ')
    score = eval(input('Enter a student score: '))

    if score > score1:
        score2, name2 = score1, name1
        score1, name1 = score, name

    elif score > score2:
        score2, name2 = score, name
    print("---------------------------")
    print("Top two Students:")
    print('Top one :-')
    print("Top one name:", name1)
    print("Top one score:", score1)
    print('Top two:-')
    print("Top two name:", name2)
    print("Top two score:", score2)
    break
