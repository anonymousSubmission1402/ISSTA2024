
def if_contains_anagrams(string_list):
    # Get the number of strings in the list
    num_strings = len(string_list)
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0
    # Iterate over each string in the list
    for i in range(num_strings):
        # Get the current string
        string1 = string_list[i]
        # Convert the current string to lowercase
        string1_lowercase = string1.lower()
        # Iterate over each subsequent string in the list
        for j in range(i + 1, num_strings):
            # Get the next string
            string2 = string_list[j]
            # Convert the next string to lowercase
            string2_lowercase = string2.lower()
            # Check if the current strings are anagrams of each other
            if sorted(string1_lowercase) == sorted(string2_lowercase):
                # Increment the counter for the number of anagrams found
                num_anagrams += 1
    # Return whether or not there are at most 113 pairs of anagrams in the given list
    return num_anagrams <= 113
