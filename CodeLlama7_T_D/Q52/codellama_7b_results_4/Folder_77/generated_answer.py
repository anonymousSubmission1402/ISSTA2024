
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the string

    for i in range(len(string)):

        # Check if the substring starting at position i and having length n is a palindrome

        substr = string[i:i+n]

        if substr == substr[::-1]:

            # If it is, add it to the set of palindromes

            palindromes.add(substr)

    # Return the set of palindromes

    return palindromes
