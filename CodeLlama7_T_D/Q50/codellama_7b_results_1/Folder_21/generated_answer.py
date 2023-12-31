
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagram pairs found
    anagram_pair_count = 0

    # Loop through each string in the list
    for i in range(len(my_list)):

        # Get the current string and its length
        current_string = my_list[i]
        current_length = len(current_string)

        # If the current string is at least three characters long, continue checking for anagrams
        if current_length >= 3:

            # Loop through each string in the list again
            for j in range(len(my_list)):

                # Get the other string and its length
                other_string = my_list[j]
                other_length = len(other_string)

                # If the other string is at least three characters long, continue checking for anagrams
                if other_length >= 3:

                    # Check if the current string and other string are anagrams
                    if sorted(current_string) == sorted(other_string):

                        # If they are anagrams, increment the counter for the number of anagram pairs found
                        anagram_pair_count += 1

                        # If there are at least 136 pairs of anagrams in the list, return true
                        if anagram_pair_count >= 136:
                            return True

    # If there are no more pairs of anagrams to check for, return false
    return False
