
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagram pairs
    pair_count = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Loop through each string after the current one
        for j in range(i + 1, len(my_list)):
            # Get the next string
            next_string = my_list[j]

            # Check if the current and next strings are anagrams
            if sorted(current_string.lower()) == sorted(next_string.lower()):
                # Increment the pair counter
                pair_count += 1

                # If we have at least 40 pairs, return True
                if pair_count >= 40:
                    return True
