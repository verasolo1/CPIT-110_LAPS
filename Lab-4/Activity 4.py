'''
Activity 3 (Problem 3)
If you know balance the annual percentage interest rate, you can compute the interest on the next monthly payment
using the following formula:
----
interest = balance * (annualInterestRate / 1200)
----
write a program that reads the balance and the annual percentage interest rate
and displays the interest to the next month.
'''
while True:
 i= 1
 balance = eval(input('enter balance : '))
 interest_Rate = eval(input('enter interest rate (%) : '))

 the_interest = (balance * interest_Rate) / 1200

 print( 'the interest is', the_interest )
 if balance == i:
     break