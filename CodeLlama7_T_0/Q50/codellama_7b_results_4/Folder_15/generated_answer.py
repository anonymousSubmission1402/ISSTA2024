
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_chars = False
    # Iterate over the list of strings
    for string in my_list:
        # Check if the string has at least three characters
        if len(string) >= 3:
            three_or_more_chars = True
            # Create a copy of the string with all lowercase letters
            lowercase_string = string.lower()
            # Iterate over the list of strings again
            for other_string in my_list:
                # Check if the other string is not the same as the current string
                if other_string != string:
                    # Create a copy of the other string with all lowercase letters
                    lowercase_other_string = other_string.lower()
                    # Check if the two strings are anagrams of each other
                    if sorted(lowercase_string) == sorted(lowercase_other_string):
                        # Increment the anagram count
                        anagram_count += 1
                        # If there are at least four pairs of anagrams, return True
                        if anagram_count >= 4:
                            return True
    # If there are no three or more character strings in the list, return False
    if not three_or_more_chars:
        return False
