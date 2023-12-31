
def palindromes_of_specific_lengths(string):
    # Create a set to store the palindromes
    palindromes = set()
    
    # Iterate over the string and check if each substring is a palindrome
    for i in range(13, 96):
        for j in range(i+57, i+60+1):
            substr = string[i:j]
            if len(substr) > 2 and substr == substr[::-1]:
                palindromes.add(substr)
    
    # Return the set of palindromes
    return palindromes
