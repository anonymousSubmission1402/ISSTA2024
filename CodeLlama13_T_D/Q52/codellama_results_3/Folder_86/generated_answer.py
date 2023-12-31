
def palindrome_of_length_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate through the string and check if each substring of length n is a palindrome
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    
    # Return the set of palindromes
    return palindromes
