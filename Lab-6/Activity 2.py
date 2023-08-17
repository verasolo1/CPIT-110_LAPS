'''
Activity 2 (Problem 2)
----
Write a program that generates two integers under 100 and prompts the user to enter the
sum of these two integers. The program then reports true if the answer is correct, false
otherwise. Also, the program displays the correct result if the answer was wrong.

'''
while True:
 i = 0
 import random

 n1 = random.randint (0, 99)
 n2 = random.randint (0, 99)

 sum = (n1 + n2)

 answer = eval(input('what is ' + str(n1) + '+' + str (n2) + ' : '))

 if sum == answer:
     print(True)
 else:
     print(False)
 if answer == i:
     break
