'''
financial application : monetary units
3.8 - 107
'''
while True:
 i= 1
 balance = eval(input('enter balance : '))
 interest = eval(input('enter interest : '))

 the_interest = (balance * interest) / 1200

 print( 'the interest is', the_interest )
 if balance == i:
     break
