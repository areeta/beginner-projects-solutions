# Change Calculator

# Imagine that your friend is a cashier, but has a hard time
    # counting back change to customers.
# Create a program that allows him to input a certain amount of
# change, and then print how how many quarters, dimes, nickels,
# and pennies are needed to make up the amount needed.
# Example: if he inputs 1.47, the program will say that he needs
    # 5 quarters, 2 dimes, 0 nickels, and 2 pennies.

# Subgoals:
    # So your friend doesn’t have to calculate how much change is needed,
        # allow him to type in the amount of money given to him and the price
        # of the item. The program should then tell him the amount of each
        # coin he needs like usual.
    # To make the program even easier to use, loop the program back to the top
        # so your friend can continue to use the program without having to close
        # and open it every time he needs to count change.

change = float(input("Enter your change (type quit to quit): "))

pennies = 0.01
nickels = 0.05
dimes = 0.10
quarters = 0.25

statement = [0, 0, 0, 0]

while change != "quit":
    if change >= 0.25:
        statement[0] = int(change/quarters)
        change -= round((int(change/quarters) * quarters), 2)
    if change < 0.25:
        statement[1] = int(change/dimes)
        change -= round((int(change/dimes) * dimes), 2)
    if change % 0.05 == 0:
        change = round(change, 2)
        statement[2] = int(change/nickels)
        change -= round((int(change/nickels) * nickels), 2)
    if change < 0.05:
        change = round(change, 2)
        statement[3] = int(change/pennies)
        change -= round((int(change/pennies) * pennies), 2)

    print(str(statement[0]) + " quarter(s), " +
          str(statement[1]) + " dime(s), " +
          str(statement[2]) + " nickel(s), " +
          str(statement[3]) + " penny/pennies" 
        )
    
    statement = [0, 0, 0, 0]
    change = float(input("Enter your change (type quit to quit): "))
    


    

        
