'''
Activity 3 (Problem 3)
----
Suppose you shop for rice and find it in two different-sized packages. You would like to
write a program to compare the costs of the packages. The program prompts the user to
enter the weight and price of each package and then displays the one with the better
price.
'''
w1, p1 = eval(input('Enter weight and price for package 1 : '))
w2, p2 = eval(input('Enter weight and price for package 2 : '))

wp1 = w1/p1
wp2 = w2/p2

if wp1 < wp2:
    print('package 1 has the better price')
else:
    print('package 2 has the better price')
