# Coin Estimator By Weight

# Allow the user to input the total weight of each type of
    # coin they have (pennies, nickels, dimes, and quarters).
# Print out how many of each type of coin wrapper they would need,
    # how many coins they have, and the estimated total value of
    # all of their money.
# Subgoals:
    # Round all numbers printed out to the nearest whole number.
    # Allow the user to select whether they want to submit the
        # weight in either grams or pounds.

# This is based on American standards.
# User input should accurate to the coin amounts.

user = input("Would you like to use grams or pounds? ")

p_weight = float(input("Input weight of pennies: "))
n_weight = float(input("Input weight of nickels: "))
d_weight = float(input("Input weight of dimes: "))
q_weight = float(input("Input weight of quarters: "))

if user == "grams":
    p_amount = p_weight/2.5
    n_amount = n_weight/5.0
    d_amount = d_weight/2.268
    q_amount = q_weight/5.67
elif user == "pounds":
    p_amount = p_weight/0.00551156
    n_amount = n_weight/0.0110231
    d_amount = d_weight/0.0050000841
    q_amount = q_weight/0.01250021

def find_total(p, n, d, q) -> int:
    total = (p*0.01) + (n*0.05) + (d*0.10) + (q*0.25)
    return round(total, 2)

print("Penny wrapper(s) needed: " + str(int(p_amount/50)))
print("Nickel wrapper(s) needed: " + str(int(n_amount/40)))
print("Dimes wrapper(s) needed: " + str(int(d_amount/50)))
print("Quarters wrapper(s) needed: " + str(int(q_amount/40)))

print("Total amount of coins: " + str(int(p_amount + n_amount + d_amount + q_amount)))

print("Total value of your money: " +
      str(find_total(p_amount, n_amount, d_amount, q_amount)))


      



