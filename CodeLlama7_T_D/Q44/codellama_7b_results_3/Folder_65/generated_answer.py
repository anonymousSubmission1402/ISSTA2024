
def composite_nums_between_indices(my_list):
    # Initialize an empty set to store the composite numbers
    composite_nums = set()

    # Iterate over the list from index 82 to index 86, both inclusive
    for i in range(82, 87):

        # Check if the current number is a prime number
        if my_list[i] == 1:

            # If it is not a prime number, then it is a composite number
            composite_nums.add(my_list[i])

    return composite_nums
