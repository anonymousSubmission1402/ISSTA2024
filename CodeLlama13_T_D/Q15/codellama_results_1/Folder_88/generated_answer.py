
def sum_odd_ints_inclusive(my_list):
    # Initialize a variable to store the sum of odd integers
    sum = 0

    # Iterate over the list and check if each integer is odd
    for i in range(4, 9):
        if my_list[i] % 2 != 0:
            sum += my_list[i]

    # Return the sum of odd integers
    return sum
