# 99 Bottles

# Create a program that prints out every line to the song "99 bottles of beer on the wall."
# Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
# Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
# Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

for x in range(99, 0, -1):
    if x == 1:
        print(x, "bottle of beer on the wall", x, "bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    else:
        print(x, "bottles of beer on the wall,", x, "bottles of beer.")
        print("Take one down and pass it around,", x-1, "bottles of beer on the wall.")
    print("\n")
