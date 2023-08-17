'''
From The Textbook
Programming exercises
2.4
2.6
2.10
--
Listing 2.10 - page 73
'''
import turtle

# prompt the user for inputting two points
x1, y1 = eval(input('enter x1 and y1 for point 1: '))
x2, y2 = eval(input('enter x2 and y2 for point 2: '))

# Compute the distance
distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Display two points and the connecting line
turtle.penup()
turtle.goto(x1,y1) #Move to (x1,y1)
turtle.pendown()
turtle.write('Point 1')
turtle.goto(x2,y2) #Drawing a line Because we didn't write pendown
turtle.write('Point 2')

# Move to the center point of the line
turtle.penup()
turtle.goto((x1 + x2) / 2, (y1 + y2) / 2)
turtle.write(distance)

turtle.goto(100,100)
turtle.write('Shady Waleed Mulla - cpit 110')

turtle.done()
