
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    min_length = 3

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]

        # Check if the current string is at least three characters long
        if len(curr_str) >= min_length:
            # Convert the current string to lowercase
            lowercase_str = curr_str.lower()

            # Iterate over the remaining strings in the list
            for j in range(i + 1, len(my_list)):
                # Get the next string
                next_str = my_list[j]

                # Check if the next string is at least three characters long
                if len(next_str) >= min_length:
                    # Convert the next string to lowercase
                    lowercase_next_str = next_str.lower()

                    # Check if the current string and the next string are anagrams of each other
                    if sorted(lowercase_str) == sorted(lowercase_next_str):
                        # Increment the number of pairs found
                        num_pairs += 1

                        # If we have found at least 18 pairs, return True
                        if num_pairs >= 18:
                            return True
    # If we have not found at least 18 pairs, return False
    return False
