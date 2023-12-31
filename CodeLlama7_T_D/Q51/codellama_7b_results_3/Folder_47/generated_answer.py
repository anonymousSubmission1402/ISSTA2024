
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        string = string.lower()
        # Sort the characters in the string
        sorted_chars = "".join(sorted(string))
        # Check if the anagram pair already exists in the dictionary
        if sorted_chars in anagram_pairs:
            # Increment the count of the anagram pair
            anagram_pairs[sorted_chars] += 1
        else:
            # Add the anagram pair to the dictionary with a count of one
            anagram_pairs[sorted_chars] = 1
    # Check if there are at most three hundred sixty-six pairs of anagrams in the list
    return len(anagram_pairs) <= 366
