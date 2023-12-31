
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list of positive integers
    for i in range(19, 93):
        # Check if the current number is divisible by any number between 2 and its square root
        for j in range(2, int(my_list[i]) ** 0.5 + 1)):
            if my_list[i] % j == 0:
                # If it is divisible, add it to the set of composite numbers
                composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the specified range
    return composite_nums
