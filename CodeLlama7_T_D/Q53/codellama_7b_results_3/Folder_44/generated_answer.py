
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting at index i and ending at the end of the string
        substr = string[i:]
        # Loop through each character in the reversed substring
        for j in range(len(substr)-1, -1, -1):
            # If the current character is not equal to the previous character, break out of the loop
            if substr[j] != substr[j-1]:
                break

            # Otherwise, add the palindrome to the set of palindromes
            else:
                palindromes.add(substr)

    # Return the set of palindromes with a length greater than or equal to n
    return palindromes
