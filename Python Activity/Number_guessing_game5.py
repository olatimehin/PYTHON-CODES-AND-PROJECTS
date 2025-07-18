'''Problem Statement:
Create a game in which user guesses a random number in python.

Questions:
- How will U generate random number and how will you set the range?
- How to add attempts in your code, that user can have only 5 attempts to play?
- How will you subtract aN attempt when user plays it one time?
- How will you show the ‘YOU WON!’ and ‘YOU LOST’ message?'''

import random

number = random.randint(0, 100)
print("Number:", number )

trials = 5
message = "You lost!"

while trials > 0:
    print(f"{trials} attempt left.")
    trials -=1 
    user_input = int(input("Enter Number: "))

    if user_input == number:
        message = "You Won!"
        break
    else:
        print("Try again")
        continue
print(message)


