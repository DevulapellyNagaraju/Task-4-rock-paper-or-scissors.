from game_logic import get_user_choice, get_computer_choice, determine_winner
from ascii_art import display_choice
from ansi_colors import RED, PINK, YELLOW, RESET

def play_game():
    print("= = = = = = = ===  Welcome to Rock-Paper-Scissors Game!  === = = = = = = =")
    user_score = 0
    computer_score = 0
    round_number = 1
    
    while True:
        print(f"\n{RED}Round {round_number}:{RESET}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}\n{display_choice(user_choice)}")
        print(f"Computer chose: {computer_choice}\n{display_choice(computer_choice)}")
        
        result, user_round_score, computer_round_score = determine_winner(user_choice, computer_choice)
        print(result)
        
        user_score += user_round_score
        computer_score += computer_round_score
        
        print(f"\n{PINK}Current Score:{RESET}")
        print(f"You: {user_score}  Computer: {computer_score}")
        
        round_number += 1
        play_again = input("Do you want to play another round? (y/n): ").lower()
        while play_again not in ['y', 'n']:
            print(f"{RED}Invalid input. Please enter 'y' or 'n'.{RESET}")
            play_again = input("Do you want to play another round? (y/n): ").lower()
        if play_again != 'y':
            print(f"\n{YELLOW}Final Score:{RESET}")
            print(f"You: {user_score}  Computer: {computer_score}")
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
