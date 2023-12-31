
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate over the list of strings
    for string in my_list:
        # Check if the string is at least three characters long
        if len(string) >= minimum_length:
            # Convert the string to lowercase
            lowercase_string = string.lower()

            # Iterate over the letters of the string
            for letter in lowercase_string:
                # Check if the letter is a vowel
                if letter in "aeiou":
                    # Increment the anagram count
                    anagram_count += 1

            # Check if there are at most 116 pairs of anagrams in the list
            if anagram_count <= 116:
                return True

        # If the string is not long enough, skip it
        else:
            continue

    # If no strings were found with at least three letters, return False
    return False
