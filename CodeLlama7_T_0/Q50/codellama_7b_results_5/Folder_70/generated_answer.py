
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Check if the string is at least three letters long
        if len(lowercase_string) >= 3:
            # Set the flag to True
            three_or_more_letters = True
            # Create a list of all the letters in the string
            letter_list = [char for char in lowercase_string]
            # Sort the list of letters
            sorted_letter_list = sorted(letter_list)
            # Check if there are any anagrams in the list
            for i in range(len(sorted_letter_list) - 1):
                # If the current letter is not the same as the next letter, continue to the next iteration
                if sorted_letter_list[i] != sorted_letter_list[i + 1]:
                    continue

                # If we reach this point, it means that there are at least two letters in a row that are the same. This is an anagram.
                anagram_count += 1

                # If we have found at least 189 pairs of anagrams, return True immediately.
                if anagram_count >= 189:
                    return True

        # If the string is not at least three letters long, continue to the next iteration.
        else:
            continue

    # If we reach this point, it means that there are no anagrams in the list. Return False immediately.
    return False
