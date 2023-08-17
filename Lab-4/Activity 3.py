'''
Activity 3 (problem 3)
write a program that reads the subtotal and the gratuity rate and computes the gratuity and total.
'''
while True:
 i = 0
 subtotal = eval(input('enter the subtotal of the gratuity : '))
 gratuityRate = eval(input('ender the gratuity rate (%) : '))
 grtaity = (subtotal / 100) * gratuityRate
 total = subtotal + grtaity
 print('the gratuity is', grtaity, 'and the total is', total)
 if subtotal == i:
      break
