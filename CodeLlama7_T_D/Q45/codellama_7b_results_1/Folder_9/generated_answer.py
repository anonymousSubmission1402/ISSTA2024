
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome between indices 0 and 6 (inclusive)
    for i in range(7, len(string)):
        # Check if the substring starting at index 0 and having length i is a palindrome
        if string[0:i] == string[0:i][::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(string[0:i])
    # Return the set of palindromes
    return palindromes
