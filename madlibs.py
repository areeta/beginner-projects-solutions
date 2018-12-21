# Mad Libs Story Maker

# Create a Mad Libs style game, where the program asks the user for
    # certain types of words, and then prints out a story with the
    # words that the user inputted.
# The story doesn't have to be too long, but it should have some sort of story line.
# Subgoals:
    # If the user has to put in a name, change the first letter to a capital letter.
    # Change the word "a" to "an" when the next word in the sentence begins with a vowel.

adj1 = input("Adjective #1: ")
adj2 = input("Adjective #2: ")
adverb = input("Adverb: ")
noun1 = input("Noun #1: ")
noun2 = input("Noun #2: ")
number = input("Number: ")
body_part = input("Part of the Body: ")
person1 = input("Person You Know #1: ")
pnoun1 = input("Plural Noun #1: ")
liquid = input("Type of Liquid: ")

print("Dear Physical Education Teacher, \n" +
      "Please excuse my son/daughter from missing " + adj1 +
      " class yesterday. When " + person1.capitalize() + " awakened yesterday, I could" +
      " see that his/her nose was " + adj2 + ". He/She also complained of " +
      body_part + " aches and having a sore " + noun1 + " and I took him/her " +
      " to the family " + noun2 + ". The doctor quickly diagnosed it to be the " +
      str(number) + "-hour flu and suggested he/she take two " + pnoun1 +
      " with a glass of " + liquid + " go to bed " + adverb + "."
)

