"""
Activity 1 (Problem 1)
----
The two roots of a quadratic equation, for example ( a * x**2 + b * x + c = 0 ) , can be obtained
using the following formula:
----
Two Roots: r1 = -b + math.sqrt(b**2 - 4ac)\  and  r2 = -b - math.sqrt(b**2 - 4*a*c)\
                            2a                                       2a
----
( b**2 - 4*a*c )is called the discriminant of the quadratic equation. ((If it is positive, the equation
has two real roots.)) ((If it is zero, the equation has one root.)) ((If it is negative, the equation has
no real roots.))
----
One Root: r1 = -b\
               2*a
----
Write a program that prompts the user to enter values for a, b, and c and displays the
result based on the discriminant. If the discriminant is positive, display two roots. If the
discriminant is 0, display one root. Otherwise, display The equation has no real roots.
"""
import math

a, b, c = eval(input('( Enter a, b, c ) : '))

Discriminant = (b ** 2 - 4 * a * c)

if Discriminant < 0:
    print("The equation has no real roots")
elif Discriminant == 0:
    r1 = -b / (2 * a)
    print("This equation has one root = " + str(r1))
else:
    r1 = (-b + math.sqrt(Discriminant)) / (2 * a)
    r2 = (-b - math.sqrt(Discriminant)) / (2 * a)
    print("This equation has two roots = ", r1, "and", r2)
