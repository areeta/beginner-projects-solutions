# Mean, Median, and Mode

# In a set of numbers, the mean is the average, the mode is the number
    # that occurs the most, and if you rearrange all the numbers numerically,
    # the median is the number in the middle.

# Create three functions that allow the user to find the mean, median, and
    # mode of a list of numbers. If you have access or know of functions that
    # already complete these tasks, do not use them.

# Subgoals
    # In the mean function, give the user a way to select how many decimal
        # places they want the answer to be rounded to.
    # If there is an even number of numbers in the list, return both numbers
        # that could be considered the median.
    # If there are multiple modes, return all of them.

def mean(num: list) -> int:
    """ This function finds the mean in a list"""
    decimal_place = int(input("How many decimal places do you it to be rounded to?"))
    sum = 0
    for n in num:
        sum += n
    return round(sum/len(num), decimal_place)

def median(num: list) -> int:
    """This function finds the median in a list"""
    num = sorted(num)
    if len(num) % 2 == 0:
        return num[int(len(num)/2)]-1, num[int(len(num)/2)]
    else:
        return num[int(len(num)/2)]
    
def mode(num: list) -> int:
    """This function finds the mode in a list"""    
    highest_count = 0
    highest_num = 0
    
    current_count = 0
    current_num = num[0]
    
    for x in num:
        if x == current_num:
            current_count += 1
            if current_count > highest_count:
                highest_count = current_count
                highest_num = current_num
        else:
            current_num = x
            current_count = 1
            
    return highest_num
