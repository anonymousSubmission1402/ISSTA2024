
def find_subset_of_length_n(set_of_elements):
    # Initialize a counter variable to keep track of the number of subsets
    count = 0

    # Iterate over all possible combinations of elements in the set
    for i in range(1 << len(set_of_elements)):

        # Check if the current combination has exactly n elements
        if bin(i).count('1') == n:

            # Increment the counter by 1 if the condition is met
            count += 1

    return count
