# ASCII art for Rock, Paper, Scissors
rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def display_choice(choice):
    if choice == "rock":
        return rock_art
    elif choice == "paper":
        return paper_art
    elif choice == "scissors":
        return scissors_art
