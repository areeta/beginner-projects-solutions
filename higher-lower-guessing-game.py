# Higher Lower Guessing Game

# Create a simple game where the computer randomly selects
    # a number between 1 and 100 and the user has to guess what
    # the number is.
# After every guess, the computer should tell the user if the guess
    # is higher or lower than the answer.
# When the user guesses the correct number, print out a congratulatory
    # message.

# Subgoals:
    # Add an introductory message that explains to the user how to play
        # your game.
    # In addition to the congratulatory message at the end of the game,
        # also print out how many guesses were taken before the user arrived
        # at the correct answer.
    # At the end of the game, allow the user to decide if they want to play
        # again (without having to restart the program).

import random

print("""
        Welcome to the Higher Lower Guessing Game! You, the user,
        gets to guess the computer's secret number between 1 and 100
        and along the way, there will be hints to let you know if the
        guess is higher or lower than the answer
    """)

run = ""

while run != "no":
    guess_count = 0
    secret_num = random.randint(1, 100)
    user_guess = int(input("Guess a number (*quit* to quit) : "))

    while user_guess != secret_num:
        if user_guess > secret_num:
            print("Guess is too high!")
        elif user_guess < secret_num:
            print("Guess is too low!")
        guess_count += 1
        user_guess = int(input("Guess another number: "))
        
    print("You got it correct! You had", guess_count, "guesse(s).")
    run = input("Game ended. Play again? (yes/no) ")
