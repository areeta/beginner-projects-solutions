# Rock Paper Scissors Game

# Create a rock-paper-scissors game.
# Ask the player to pick rock, paper or scissors.
# Have the computer chose its move.
# Compare the choices and decide who wins.
# Print the results.
# Subgoals:
    # Give the player the option to play again.
    # Keep a record of the score (e.g. Player: 3 / Computer: 6).

import random

comp_wins = 0
user_wins = 0

def determine_winner(user_move, comp_move):
    global comp_wins
    global user_wins
    if user_move == "scissors" and comp_move == "rock":
        comp_wins += 1
    elif user_move == "paper" and comp_move == "rock":
        user_wins += 1
    elif user_move == "rock" and comp_move == "paper":
        comp_wins += 1
    elif user_move == "scissors" and comp_move == "paper":
        user_wins += 1
    elif user_move == "rock" and comp_move == "scissors":
        user_wins += 1
    elif user_move == "paper" and comp_move == "scissors":
        comp_wins += 1
    print("Computer:", comp_wins, "User:", user_wins)
        
if __name__ == '__main__':
    print("Welcome to Areeta's Rock Paper Scissors Game!")
    user_move = input("What is your move? Pick between rock, " +
                      "paper, or scissors? Type quit to quit the game: ")

    comp_moves = ["rock", "paper", "scissors"]
    comp_move = random.choice(comp_moves)

    while user_move != "quit":
        print("Computer played:", comp_move, "User played:", user_move)
        determine_winner(user_move, comp_move)
        user_move = input("Would you like to play again? (yes/no) ")
        if user_move == "yes":
            user_move = input("What is your move? Pick between rock, paper," +
                          " or scissors? ")
        else:
            user_move = "quit"
        

