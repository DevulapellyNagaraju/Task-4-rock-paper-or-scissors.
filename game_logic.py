import random
from ansi_colors import GREEN, RED, PINK, YELLOW, RESET
from ascii_art import display_choice

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print(f"{RED}Invalid choice. Please choose again.{RESET}")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return f"{GREEN}You win!{RESET}", 1, 0  # Green color for "You win!"
    else:
        return f"{RED}You lose!{RESET}", 0, 1  # Red color for "You lose!"
