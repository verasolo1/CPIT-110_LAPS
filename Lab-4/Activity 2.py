'''
activity 2 (problem 2)
Write a program that reads in an investment amount, the annual interest rate, and the
number of years, and displays the future investment value using the following formula:
futureInvestmentValue = investAmount * (1 + monthlyInterestRate) ** numberOfmonths
'''
while True:
 i = 1
 investmentAmount = eval(input('enter the investment amount : '))
 annualInterestRate = eval(input('enter the annul interest rate (%) : '))
 numberOFyears = eval(input('enter the number of years as an integer : '))

 monthlyInterestRate = (annualInterestRate / 100) / 12
 numberOFmonths = numberOFyears * 12

 futureInvestmentvalue = investmentAmount * \
                        ((1 + monthlyInterestRate) ** numberOFmonths)

 print('Future value is', int(futureInvestmentvalue * 100 / 100.0))
 if investmentAmount == i:
     break
