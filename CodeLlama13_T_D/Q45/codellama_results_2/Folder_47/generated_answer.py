
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length 5 that occurs between indices 3 and 7, both inclusive
    for i in range(3, 8):
        for j in range(i + 1, min(len(string), 8)):
            substring = string[i:j]
            
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    # Return the set of palindromes
    return palindromes
