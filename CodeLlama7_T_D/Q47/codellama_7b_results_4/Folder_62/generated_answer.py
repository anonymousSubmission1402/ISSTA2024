
def palindromes_of_specific_lengths(string):
    # Define the substring and palindrome lengths
    substring = string[26:87]
    palindrome_lengths = range(52, 57)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its index
        char = substring[i]
        index = i + 26
        # Check if the current character is a palindrome with one of the specified lengths
        for length in palindrome_lengths:
            if index + length <= len(substring):
                substr = substring[index:index+length]
                if substr == substr[::-1]:
                    palindromes.add(substr)
    # Return the set of palindromes found in the substring
    return palindromes
