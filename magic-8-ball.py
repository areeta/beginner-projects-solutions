# Magic 8 Ball

# Simulate a magic 8-ball.
# Allow the user to enter their question.
# Display an in progress message(i.e. “thinking”).
# Create 20 responses, and show a random response.
# Allow the user to ask another question or quit.

# Bonus:
    # Add a gui.
    # It must have box for users to enter the question.
    # It must have at least 4 buttons:
        # ask
        # clear (the text box)
        # play again
        # quit (this must close the window)

import random
import time


def shake() -> str:
    answers = [
                    "It is certain.", "It is decidedly so.", "Without a doubt.",
                    "Yes - definitely.", "You may rely on it.", "As I see it, yes.",
                    "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.",
                    "Signs point to yes.", "Reply hazy, try again.", "Ask again later.",
                    "Better not tell you now.", "Cannot predict now.",
                    "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
                    "My sources say no.", "Outlook not so good.", "Very doubtful."
              ]
    choice = random.randint(0, 20)
    return answers[choice]

if __name__== "__main__":
    user = input("What is your question for the Magic 8 Ball? Type *quit* to quit: ")
    print("Thinking...")
    time.sleep(1)
    while user != "quit":
        print("Your fortune is:", shake())
        user = input("What is your question for the Magic 8 Ball? Type *quit* to quit: ")
    

    
