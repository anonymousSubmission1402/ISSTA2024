
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a whitespace or a punctuation)
        if string[i].isalpha():
            # Get the substring of length n starting from the current character
            substring = string[i:i+n]
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    # Return the set of all palindromes of length n as substrings of the given string
    return palindromes
