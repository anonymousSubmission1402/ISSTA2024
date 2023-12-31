
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Loop through the list of positive integers
    for i in range(len(my_list)):
        # Check if the current number is composite
        if is_composite(my_list[i]):
            # If it is, add it to the set of composite numbers
            composite_nums.add(my_list[i])

    # Return the set of all composite numbers in the given list that are between index 8 to index 9, both inclusive
    return composite_nums

# Define a function to check if a number is composite
def is_composite(n):
    # Check if n is greater than 1
    if n > 1:
        # Loop from 2 to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # If the current number is a factor of n, return False
            if n % i == 0:
                return False

    # If no factors are found, return True
    return True
