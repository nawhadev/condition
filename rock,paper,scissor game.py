import random

def display_rules():
    print("\n--- Game rules ---")
    print("Rock beats Scissor")
    print("Paper beats Rock")
    print("Scissor beats Paper\n")
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper") or \
        return "user"
    else:
        return "computer"
def rock_paper_scissors():
    total_choices= ["rock" , "paper" , "scissor"]

    while True:
        user_score = 0
        computer_score = 0
        round_number = 1

        print("\n Welcome to the Rock-Paper-Scissor Game!")
        print("Type 'rules' to see how to play, or 'quit' to exit the game.\n")