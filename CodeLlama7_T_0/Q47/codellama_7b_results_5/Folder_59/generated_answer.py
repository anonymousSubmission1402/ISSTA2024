
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from index i to index 100 (both inclusive)
        substring = string[i:101]
        # Loop through each length of palindrome between 3 and 15 (both inclusive)
        for length in range(3, 16):
            # Get the substring of the specified length from the current position in the string
            substr = substring[:length]
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    # Return the set of palindromes found in the specified index range and with the specified lengths
    return palindromes
