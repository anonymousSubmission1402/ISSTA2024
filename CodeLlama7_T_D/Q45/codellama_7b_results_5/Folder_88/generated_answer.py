
def palindromes_between_indices(string):
    # Create a list of all possible palindromes of length at least 6
    palindromes = []
    for i in range(3, len(string) - 2):
        # Check if the substring starting at index i and ending at index (i + 5) forms a palindrome
        substr = string[i:i + 6]
        if substr == substr[::-1]:
            palindromes.append(substr)
    return set(palindromes)
