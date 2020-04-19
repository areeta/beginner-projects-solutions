# Fibonacci Sequence

# Define a function that allows the user to find the value of the nth term
    # in the sequence.
# To make sure you’ve written your function correctly, test the first 10
    # numbers of the sequence.
# You can assume either that the first two terms are 0 and 1 or that they
    # are both 1.
# There are two methods you can employ to solve the problem. One way is
    # to solve it using a loop and the other way is to use recursion.
# Try implementing a solution using both methods.

def findNth(nth: int) -> int:
    if nth == 0:
        return 0
    elif nth == 1:
        return 1
    else:
        return findNth(nth - 1) + findNth(nth - 2)

print(findNth(6))
