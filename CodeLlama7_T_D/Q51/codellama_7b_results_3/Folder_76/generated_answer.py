
def if_contains_anagrams(my_list):
    # create a dictionary to store the number of occurrences of each anagram
    anagram_counts = {}

    # loop through the list of strings
    for string in my_list:
        # convert the string to lowercase for case-insensitive comparison
        lowercase_string = string.lower()

        # check if the string is a palindrome (i.e., it reads the same backwards and forwards)
        is_palindrome = lowercase_string == lowercase_string[::-1]

        # check if the string contains only English letters (a-z or A-Z)
        is_english_letter_only = all(c.isalpha() for c in lowercase_string)

        # check if the string has a length of at least three
        is_length_at_least_three = len(lowercase_string) >= 3

        # if the string meets all the criteria, add it to the dictionary of anagram counts
        if is_palindrome and is_english_letter_only and is_length_at_least_three:
            # split the string into a list of individual characters
            characters = [c for c in lowercase_string]

            # sort the list of characters
            sorted_characters = sorted(characters)

            # join the sorted list of characters back into a single string
            sorted_character_string = "".join(sorted_characters)

            # add one to the count for this anagram, if it already exists in the dictionary
            if sorted_character_string in anagram_counts:
                anagram_counts[sorted_character_string] += 1

            # otherwise, set the count for this anagram to one
            else:
                anagram_counts[sorted_character_string] = 1

    # return True if there are at most 91 pairs of anagrams in the given list
    return len(anagram_counts) <= 91
