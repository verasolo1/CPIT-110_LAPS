'''
From The Textbook
Programming exercises
2.4
2.6
2.10
--
Listing 2.6 - page 66
'''
while True:
 i = 0
# Prompt the user for input
 purchaseAmount = eval(input('Enter purchase amount: '))

# Compute Sales Tax
 tax = purchaseAmount * 0.06

# display tax amount with two digits after decimal point
 print('Sales tax is', int(tax * 100) / 100.0)
 if purchaseAmount == i:
     break