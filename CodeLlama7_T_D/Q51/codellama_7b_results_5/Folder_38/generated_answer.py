
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Check if the string is a palindrome
        if lowercase_string == lowercase_string[::-1]:
            # Increment the counter for anagrams found
            num_anagrams += 1
    # Return True if there are at most 416 pairs of anagrams in the given list, False otherwise
    return num_anagrams <= 416
