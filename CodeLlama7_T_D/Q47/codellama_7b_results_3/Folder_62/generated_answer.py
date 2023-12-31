
def palindromes_of_specific_lengths(string):
    # Lowercase the string for case-insensitive comparison
    string = string.lower()

    # Define the range of indices where palindromes can occur
    start_index = 26
    end_index = 87

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the string within the specified range
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter (not a space or other non-letter character)
        if string[i].isalpha():
            # Iterate over the characters in the string within the specified range starting from the current index i
            for j in range(i, end_index + 1):
                # Check if the character at index j is a letter (not a space or other non-letter character)
                if string[j].isalpha():
                    # Check if the substring starting at index i and ending at index j is a palindrome (i.e., it reads the same forward and backward)
                    if string[i:j+1] == string[i:j+1][::-1]:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(string[i:j+1])

            # Check if any palindromes have been found for the current substring starting at index i and ending at index j
            if len(palindromes) > 0:
                # Return the set of palindromes
                return palindromes

    # If no palindromes have been found in any of the substrings within the specified range, return an empty set
    return set()
