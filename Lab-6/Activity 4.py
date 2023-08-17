'''
Activity 4 (Problem 4)
----
Write a program that plays the popular scissor-rock-paper game. (A scissor can cut a
paper, a rock can knock a scissor, and a paper can wrap a rock.) The program randomly
generates a number 0, 1, or 2 representing scissor, rock, and paper. The program prompts
the user to enter a number 0, 1, or 2 and displays a message indicating whether the user
or the computer wins, loses, or draws.
----



'''
while True:

 import random
 actions = ['rock', 'paper', 'scissor']
 user = input('enter your action (rock, paper, scissor) : ' )
 computer = random.choice(actions)
 print("You chose", user, 'computer chose', computer)

 if user == computer:
     print("tie")
 elif user == "rock":
     if computer == "scissors":
         print("Rock break scissors! You Win!")
     else:
         print("Paper covers rock, You Lose.")
 elif user == "paper":
     if computer == "rock":
         print("Paper covers rock, You Win!")
     else:
         print("Scissors cuts paper, You Lose.")
 elif user == "scissors":
     if computer == "paper":
         print("Scissors cuts paper, You Win!")
     else:
         print("Rock break scissors, You Lose.")





