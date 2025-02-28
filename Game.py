# Rock, Paper, Scissors game

import random

options = ("rock", "paper", "scissors")

player = None

computer = random.choice(options)
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a TIE")
    elif player == "rock" and computer == "scissors":
        print("You win!:")
    elif player == "paper" and computer == "rock":
        print("You win!:")
    elif player == "scissors" and computer == "paper":
        print("You win!:")
    else:
        print("you lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")


