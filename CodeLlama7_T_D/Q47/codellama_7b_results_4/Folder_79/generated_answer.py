 def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(1, len(string) - 8 + 1):
        # Check if the substring starting from index i and ending at index i + 8 is a palindrome
        substr = string[i:i + 8]
        if substr == substr[::-1]:
            # Check if the length of the substring is between 3 to 4 (both inclusive)
            if len(substr) in range(3, 5):
                # Add the palindrome to the set
                palindromes.add(substr)
    return palindromes
