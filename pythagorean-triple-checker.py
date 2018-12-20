# Pythagorean Triples Checker

# If you do not know how basic right triangles work, or what a Pythagorean
    # Triple is read these articles on Wikipedia.
# Allows the user to input the sides of any triangle in any order.
# Return whether the triangle is a Pythagorean Triple or not.
# Loop the program so the user can use it more than once without having
    # to restart the program.

user = input("Enter the sides of a triangle, using a space between each number('quit' to quit): ")

while user != "quit":
    
    num_list = user.split(" ")
    for num in num_list:
        if int(num) < 0:
            print("Error. Value is less than 0.")
            break
        
    # Makes sure that each number is type int
    for x in range(len(num_list)):
        num_list[x] = int(num_list[x])
        
    if num_list[0] > num_list[1] and num_list[0] > num_list[2]:
        if (num_list[1] ** 2) + (num_list[2] ** 2) == (num_list[0] ** 2):
            print("This is a Pythagorean Triple!")
            user = input("Enter the sides of a triangle, using a space between each number ('quit' to quit): ")
    elif num_list[1] > num_list[0] and num_list[1] > num_list[2]:
        if (num_list[2] ** 2) + (num_list[0] ** 2) == (num_list[1] ** 2):
            print("This is a Pythagorean Triple!")
            user = input("Enter the sides of a triangle, using a space between each number ('quit' to quit): ")
    elif num_list[2] > num_list[0] and num_list[2] > num_list[1]:
        if (num_list[0] ** 2) + (num_list[1] ** 2) == (num_list[2] ** 2):
            print("This is a Pythagorean Triple!")
            user = input("Enter the sides of a triangle, using a space between each number ('quit' to quit): ")
    else:
        print("This is not a Pythagorean Triple")
        user = input("Enter the sides of a triangle, using a space between each number ('quit' to quit): ")
