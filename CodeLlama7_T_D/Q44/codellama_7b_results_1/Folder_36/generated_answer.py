
def composite_nums_between_indices(my_list):
    # Find the indices of the first and last composite numbers in the list
    first_composite_index = next((i for i, x in enumerate(my_list) if is_composite(x)), None)
    last_composite_index = next((i for i, x in enumerate(my_list) if is_composite(x)), None)
    # Return the set of all composite numbers between the first and last indices
    return set(my_list[first_composite_index:last_composite_index+1])
# Helper function to check if a number is composite
def is_composite(n):
    if n == 1 or n == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True

    return False
