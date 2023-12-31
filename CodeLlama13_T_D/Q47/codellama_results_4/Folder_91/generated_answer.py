
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()

    # Loop through each substring of length 3 to 5, both inclusive
    for i in range(3, 6):
        # Get the substring from index 0 to index 10, both inclusive
        substring = string[0:i]

        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)

    # Return the set of palindromes
    return palindromes
