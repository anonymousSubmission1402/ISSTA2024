
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome between indices 1 and 5
    for length in range(4, len(string) + 1):
        # Loop through each possible starting index of the palindrome
        for start in range(1, len(string) - length + 2):
            # Check if the substring starting at 'start' and ending at 'start + length - 1' is a palindrome
            if string[start:start + length] == string[start:start + length][::-1]:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[start:start + length])
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
