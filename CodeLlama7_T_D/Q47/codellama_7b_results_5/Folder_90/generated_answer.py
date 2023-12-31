
def palindromes_of_specific_lengths(string):
    # Define the range of lengths for which palindromes will be searched
    lengths = range(136, 152)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the specified range
    for length in lengths:
        # Find the first occurrence of a palindrome with the current length
        start_index = 106
        while start_index + length <= 280:
            substr = string[start_index : start_index + length]
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
            start_index += 1

    return palindromes
