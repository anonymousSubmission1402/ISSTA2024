
def palindrome_of_length_at_least_n(string, n=36):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each word in the string
    for word in string.split():
        # Check if the word is a palindrome of length greater than or equal to n
        if len(word) >= n and word == word[::-1]:
            # Add the palindrome to the set
            palindromes.add(word)
    # Return the set of all palindromes found in the string
    return palindromes
