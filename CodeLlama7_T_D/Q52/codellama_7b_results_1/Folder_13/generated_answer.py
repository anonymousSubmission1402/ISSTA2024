
def palindrome_of_length_n(string):
    # Split the string into individual characters
    chars = list(string)

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the length of the string
    for i in range(len(chars)):

        # Check if the substring starting at index i and ending at index len(string) - (i - 1) is a palindrome
        substr = "".join(reversed(chars[i:]))

        # If the substring is a palindrome, add it to the set of palindromes
        if substr == string[i:]:
            palindromes.add(substr)

    # Return the set of palindromes
    return palindromes
