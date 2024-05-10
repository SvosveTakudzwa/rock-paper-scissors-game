##Rock/Paper/Scissors Game
import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]

while True:
    user_input = input("Choose between Rock/Paper/Scissors or Press Q to quit: ")
    if user_input.lower() == "q":
        break
        
    if user_input not in options:
        continue
        
    random_number = random.randint(0,2)
    # rock:0, paper:1, scissors:2
    computer_option = options[random_number]
    if user_input == "rock" and computer_option == "scissors":
        user_wins += 1
        print("You win!")
    elif user_input == "paper" and computer_option == "rock":
        user_wins += 1
        print("You win!")
    elif user_input == "scissors" and computer_option == "paper":
        user_wins += 1
        print("You win!")
    else:
        computer_wins += 1
        print("You lose!")
        
print("You won",user_wins,"times.")
print("Computer won",computer_wins,"times.")