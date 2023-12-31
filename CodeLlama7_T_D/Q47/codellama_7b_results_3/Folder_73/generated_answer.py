
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start_index = 21
    end_index = 62

    # Create a list to store the palindromes
    palindromes = []

    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a palindrome
        if string[i] == string[i:].lower()[::-1]:
            # If it is, add it to the list of palindromes
            palindromes.append(string[i])

    # Return the set of all palindromes with the specified lengths and characters in the given substring
    return set(palindromes)
