
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each possible length of palindrome
    for i in range(4, len(string) + 1):
        # Loop through each possible starting index of the palindrome
        for j in range(0, len(string) - i + 1):
            # Check if the substring starting at index j and having length i is a palindrome
            if string[j:j+i] == string[j:j+i][::-1]:
                # Add the palindrome to the set
                palindromes.add(string[j:j+i])
    return palindromes
