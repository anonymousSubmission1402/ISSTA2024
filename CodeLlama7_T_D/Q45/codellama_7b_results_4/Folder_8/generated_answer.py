
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible combination of letters between indices 1 and 5 (inclusive)
    for i in range(1, 6):
        for j in range(i + 1, 7):
            # Check if the substring between indices i and j is a palindrome
            if string[i:j] == string[i:j][::-1]:
                # If it is, add it to the set of palindromes
                palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
