
def palindromes_between_indices(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate through each possible arrangement of letters between indices 4 and 9, both inclusive
    for i in range(4, 10):
        for j in range(i+2, 11):
            # Check if the substring formed by the letters between indices i and j is a palindrome
            substring = string[i:j]
            if substring == substring[::-1]:
                # Add the palindrome to the set
                palindromes.add(substring)
    
    # Return the set of palindromes
    return palindromes
