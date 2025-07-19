# I HAVE WRITTEN THREE DIFFERENT CODE 

# Importing the random module to generate random choices for the computer
# Displaying the game introduction and rules
# Infinite loop to keep the game running until the user decides to quit
    # Asking the user to enter their choice  
    # Taking the user's input and converting it to an integer   
    # Validation: Ensuring the user enters a valid choice between 1 and 3  
    # Assigning a name to the user's choice based on the number they selected
        # Assign "Scissor" if the user chooses option 3 
    # Printing the user's choice 
    # The computer randomly selects a choice (1 for Rock, 2 for Paper, 3 for Scissor) 
    # If the computer's choice is the same as the user's, regenerate the computer's choice    
    # Assigning a name to the computer's choice   
    # Printing the computer's choice
            # Show user vs computer choice
    # Checking the result of the game (win/draw)
            # If user and computer choose the same, it's a draw        
    # Conditions where Paper wins
            # Rock vs Paper -> Paper wins
            # Paper vs Rock -> Paper wins
    # Conditions where Rock wins
            # Rock vs Scissor -> Rock wins
            # Scissor vs Rock -> Rock wins
    # Conditions where Scissor wins
            # Paper vs Scissor -> Scissor wins
            # Scissor vs Paper -> Scissor wins"  
    # Output who the winner is
             # It's a tie
             # User wins
             # Computer wins 
    # Asking the user if they want to play again
    # If the user says "n" (no), the game ends 
    # Otherwise, the game continues

import random 

print("ROCK,PAPER,SCISSOR GAME! \n" +
      "Game Rules \n+"
      "Rock Vs Paper --> Paper Wins \n" +
      "Rock Vs Scissor --> Rock Wins \n" + 
      "Paper Vs Scissor -->Scissor Wins \n")

while True:
    
    print("Enter your choice: \n 1-Rock \n 2-Paper \n 3-Scissor")
    
    choice = int(input("Enter the choice: "))
    
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please: "))
        
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name == "Scissor"
        
    print("User choice is:", choice_name)
    print("Now its computers turn!")
    
    computer_choice = random.randint(1,3)
    
    while computer_choice == choice:
        computer_choice = random.randint(1,3)
        
    if computer_choice == 1:
        computer_choice_name = "Rock"
    elif computer_choice == 2:
        computer_choice_name = "Paper"
    else:
        computer_choice_name = "Scissors"
        
    print("Computer choice is: ", computer_choice_name)
    print(choice_name, "VS", computer_choice_name)
    
    if choice == computer_choice:
        print("Draw", end = " ")
        result = "Draw"
    if (choice ==1 and computer_choice==2):
        print("Paper Wins: ", end="")
        result = "paper"  
    elif(choice == 2 and computer_choice == 1):
        print("Paper wins", end="")
        result = "paper"
    if (choice==1 and computer_choice ==3):
        print("Rock Wins: ", end="")
        result = "Rock"
    elif (choice==3 and computer_choice==1):
        print("Rock Wins: ", end="")
        result = "Rock"
    if (choice ==2 and computer_choice==3):
        print("Scissor wins: ", end="")
        result = "Scissor" 
    elif(choice==3 and computer_choice==2):
        print("Scissor wins: ", end="")
        result="Scissor"
    if result == "Draw:":
        print("<==It's a tie==>")
    if result == choice_name:
        print("<== User wins==>")
    else:
        print("<==Computer wins ==>")
        
    answer = input("Do you want to play again? (y/n):")
    if answer == "n":
        print("Thanks for playing")
        break
    
    else:
        continue                   

# CODE TWO

# Define a list of valid moves
    # Ask the player to make their choice
     # Handle player exiting the game
     # Ensure valid input from the player
     # Get the computer's choice
     # Display the choices
     # Determine the winner and print the result
   
import random as rd

options = ["rock","paper","scissors"]


def get_computer_choice():
    return rd.choice(options)

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
        return "You Win!"
    else:
        return "computer wins!"
    
while True:
    player_choice = input("Enter Rock, Paper, or Scissors (or type 'exit' to quit): ").lower()

    if player_choice == "exit":
        print("Thanks for playing!")
        break
    if player_choice not in options:
        print("Inavlid input! Please choose Rock,Paper or Scissors.")
        continue
    
    computer_choice = get_computer_choice() # call the function get_computer_choice above
    #print(computer_choice) to confirm 
    print(f"You chose: {player_choice}")
    print(f"computer chose: {computer_choice}")
    
    result = get_winner(player_choice,computer_choice)  # call the function get_winner above 
    print(result)
    
# CODE THREE 
import random 

choices = ["rock","paper","scissors"]

computer_choice = random.choice(choices)

player_choice = input("Enter your choice (rock,paper,scissors): ").lower()

if player_choice == computer_choice:
    print(f"Both choose {player_choice}. It's a tie!")
    
elif player_choice == "rock":
    if computer_choice == "scissors":
        print("Rock beats scissors.You Win")
        
    else:
        print("paper beats Rock.You lose!")
        
elif player_choice == "paper":
    if computer_choice == "rock":
        print("paper beats rocks.You Win")
        
    else:
        print("Scissors beats paper.You lose!")
        
elif player_choice == "Scissors":
    if computer_choice == "paper":
        print("Scissors beat paper.You Win")
        
    else:
        print("rock beats scissors.You lose!")
        
else:
    print("Invalid input! please enter rock,paper, or scissors. ")
    
    
    