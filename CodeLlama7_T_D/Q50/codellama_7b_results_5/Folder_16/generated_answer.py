
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if the current string is at least three characters long
        if len(current_string) < minimum_length:
            continue

        # Convert the current string to lowercase
        current_string_lowercase = current_string.lower()

        # Loop through each string in the list again
        for j in range(len(my_list)):
            # Get the current string again
            other_string = my_list[j]

            # Check if the current string is not the same as the other string
            if i != j:
                # Convert the other string to lowercase
                other_string_lowercase = other_string.lower()

                # Check if the current string and the other string are anagrams of each other
                if sorted(current_string_lowercase) == sorted(other_string_lowercase):
                    # Increment the anagram count
                    anagram_count += 1

    # Return true if there are at least 155 pairs of anagrams in the list, or false otherwise
    return anagram_count >= 155
