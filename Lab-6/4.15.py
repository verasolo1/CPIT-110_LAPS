"""
(Game: lottery)
generate a three-digit lottery
number. The program prompts the user to enter a three-digit number and determines whether the user wins according
to the following rules:
--
1. If the user input matches the lottery number in the exact order, the award is
$10,000.
--
2. If all the digits in the user input match all the digits in the lottery number, the
award is $3,000.
--
3. If one digit in the user input matches a digit in the lottery number, the award is
$1,000.
"""
import random
R1 = random.randint(0, 99)
R2 = random.randint(0, 99)
R3 = random.randint(0, 99)
D1, D2, D3 = eval(input('enter three digits : '))
if (D1, D2, D3) == (R1, R2, R3):
    print('congrats you have WON $10,000', ',the lottery number is', R1, R2, R3)

if (D1, D2, D3) == (R1, R2, R3):
    print('congrats you have WON $1,000', ',the lottery number is', R1, R2, R3)

if (D1, D2, D3, D1, D2, R3, D1, D2, D3) == (R1, R2, R3, R1, R2, R3, R1, R2, R3):
    print('congrats you have WON $3,000', ',the lottery number is', R1, R2, R3)
else:
    print('the lottery number is', R1, R2, R3, 'good luck next time')
