 def palindromes_of_specific_lengths(string):
    # Define the range of lengths to consider
    lengths = range(154, 183)
    # Define the range of indices to consider
    indices = range(101, 293)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each length in the specified range
    for length in lengths:
        # Get the substring of the specified length starting at the first index
        substring = string[indices[0] : indices[0] + length]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
