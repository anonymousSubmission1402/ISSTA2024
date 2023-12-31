
def find_subset_of_length_n(set):
    # Initialize a counter for the number of subsets
    count = 0

    # Iterate over all possible subsets of size 21
    for i in range(1 << len(set))):
        # Check if the current subset has length 21
        if len(set & (1 << i))) == 21:
            # Increment the counter if it does
            count += 1

    # Return the number of all its subsets of size 21
    return count
