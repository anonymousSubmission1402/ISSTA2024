
def palindromes_of_specific_lengths(string):
    # Create a substring from index 17 to index 72, both inclusive
    substring = string[17:73]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the length of the current palindrome
        length = len(substring[i:])
        # Check if the length is between 50 and 51 (both inclusive)
        if 50 <= length <= 51:
            # Check if the palindrome occurs in a case-insensitive manner
            if substring[i:].lower() == substring[i:].lower()[::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(substring[i:])
    # Return the set of palindromes
    return palindromes
