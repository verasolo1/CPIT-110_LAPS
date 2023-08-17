"""
Activity 4 (problem 4)
----
Write a program that reads integers, finds the largest of them, and counts its occurrences.
Assume that the input ends with number 0. Suppose that you entered 3 5 2 5 5 5 0; the
program finds that the largest number is 5 and the occurrence count for 5 is 4.
-
Hint: Maintain two variables, max and count. The variable max stores the current
maximum number, and count stores its occurrences. Initially, assign the first number to
max and 1 to count. Compare each subsequent number with max. If the number is greater
than max, assign it to max and reset count to 1. If the number is equal to max, increment
count by 1.
"""
Break = 0
count = 0
Max = 0
while True:
    User_input = eval(input("Enter integers (Entering \'0\' will terminate the program) : "))
    if User_input >= Max:
        Max = User_input
    elif User_input == Break:
        break

print(Max)
