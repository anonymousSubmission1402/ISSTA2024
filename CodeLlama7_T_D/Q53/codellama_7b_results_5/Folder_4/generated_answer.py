
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each word in the string
    for word in string.split():
        # Check if the word is a palindrome of length greater than or equal to n
        if word == word[::-1] and len(word) >= n:
            # Add the word to the set of palindromes
            palindromes.add(word)
    # Return the set of palindromes
    return palindromes
