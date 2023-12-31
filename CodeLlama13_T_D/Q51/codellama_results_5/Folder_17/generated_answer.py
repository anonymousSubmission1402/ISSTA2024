
def if_contains_anagrams(list_of_strings):
    # Initialize a dictionary to store the anagram counts for each letter
    anagram_counts = {}
    
    # Iterate through the list of strings and check if each string is an anagram
    for string in list_of_strings:
        # Convert the string to uppercase to ensure case-insensitivity
        uppercase_string = string.upper()
        
        # Check if the string is a valid anagram by checking if it contains only English letters and has a length of at least three
        if all(letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' for letter in uppercase_string) and len(uppercase_string) >= 3:
            # If the string is a valid anagram, increment the count for each letter in the anagram
            for letter in uppercase_string:
                if letter not in anagram_counts:
                    anagram_counts[letter] = 1
                else:
                    anagram_counts[letter] += 1
    
    # Check if there are at most 22 pairs of anagrams in the list
    if len(anagram_counts) <= 22:
        return True
    else:
        return False
