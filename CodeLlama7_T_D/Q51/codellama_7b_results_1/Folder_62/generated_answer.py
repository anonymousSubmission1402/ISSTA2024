
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a valid anagram
        if is_valid_anagram(lowercase_string):
            # Add the anagram count to the dictionary
            anagram_counts[lowercase_string] = anagram_counts.get(lowercase_string, 0) + 1

    # Check if there are at most 289 pairs of anagrams in the list
    return len(anagram_counts) <= 289

# Check if a string is a valid anagram
def is_valid_anagram(string):
    # Convert the string to a list of characters
    char_list = list(string)

    # Sort the list of characters
    sorted_char_list = sorted(char_list)

    # Check if the sorted list of characters is a valid anagram
    return "".join(sorted_char_list) == string
