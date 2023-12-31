
def all_ints_div_by_num(my_list):
    # Initialize an empty list to store the divisible integers
    divisible_ints = []

    # Iterate through the list of integers and check if each integer is divisible by 1
    for i in range(10, len(my_list)):
        if my_list[i] % 1 == 0:
            # If the integer is divisible by 1, add it to the list of divisible integers
            divisible_ints.append(my_list[i])

    # Return the list of all integers divisible by 1 from index 10 to index 10, both inclusive
    return divisible_ints
