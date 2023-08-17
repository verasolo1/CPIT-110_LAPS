'''
2.21 - page 80
(financial application: compound value) Suppose you save '100$' each month into a saving account
with an annual interest rate of 5%.
--------
the monthly interest rate is 0.05/12 = 0.00417. after the first month, the value in the account becomes..
100 * (1 + 0.0.417) = 100.417
after second month ..
(100 + 100.417) * (1 + 0.00417) = 201.252
after third month
(100 + 201.252) * (1 + 0.00417) = 302.507

and so on..

fourth month
(100 + 302.507) * (1 + 0.00417) = 404.185
fifth month
(100 + 404.185) * (1 + 0.00417) = 506.287
sixth month
(100 + 506.287) * (1 + 0.00417) = 608.815
----
write a program that prompts the user to enter a monthly saving amount and
displays the account value after the sixth month.
'''
MonthlySaving = eval(input('enter the monthly saving amount : '))

x = MonthlySaving + 506.287

sixthMonth = x * (1 + 0.00417)

print('after the sixth month, the account value is', sixthMonth)