
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start = 29
    end = 96

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over each character in the string
    for i in range(start, end + 1):
        # Check if the substring starting at index i is a palindrome
        if string[i:] == string[i:][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:])

    # Return the set of palindromes that meet the requirements
    return palindromes
