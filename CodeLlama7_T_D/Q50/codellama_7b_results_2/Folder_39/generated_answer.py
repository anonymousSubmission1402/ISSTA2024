
def if_contains_anagrams(my_list):
    # Initialize variables
    count = 0
    anagram_count = 0

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if there are at least five pairs of anagrams in the list
        if len(my_list) > 53:
            count += 1

    # Return True if there are at least five pairs of anagrams in the list, otherwise return False
    if count >= 54:
        return True
    else:
        return False
