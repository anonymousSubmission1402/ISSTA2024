
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for length in range(3, len(string) + 1):
        # Generate all possible combinations of letters
        # that form palindromes of the current length
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    return palindromes
