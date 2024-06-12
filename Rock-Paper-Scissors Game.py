# Rock-Paper-Scissors Game 

import random

# Initialize scores
Player_Score = 0
Computer_Score = 0

while True:

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = ""

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

        if player == computer:
            print("Computer:", computer)
            print("Player:", player)
            print("It's a Tie!")

        elif player == "rock":
            if computer == "paper":
                print("Computer:", computer)
                print("Player:", player)
                print("You Lose!")
                Computer_Score = Computer_Score + 1
            if computer == "scissors":
                print("Computer:", computer)
                print("Player:", player)
                print("You Win!")
                Player_Score = Player_Score + 1

        elif player == "scissors":
            if computer == "paper":
                print("Computer:", computer)
                print("Player:", player)
                print("You Win!")
                Player_Score = Player_Score + 1
            if computer == "rock":
                print("Computer:", computer)
                print("Player:", player)
                print("You Lose!")
                Computer_Score = Computer_Score + 1

        elif player == "paper":
            if computer == "scissors":
                print("Computer:", computer)
                print("Player:", player)
                print("You Lose!")
                Computer_Score = Computer_Score + 1
            if computer == "rock":
                print("Computer:", computer)
                print("Player:", player)
                print("You Win!")
                Player_Score = Player_Score + 1

    print("Player Score:", Player_Score)
    print("Computer Score:", Computer_Score)

    Play_Again = input("Play Again? (yes/no): ").lower()

    if Play_Again != "yes":
        break

print("Bye")