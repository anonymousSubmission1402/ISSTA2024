
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each index in the substring from 63 to 70, both inclusive
    for i in range(63, 71):
        # Check if the substring from index i - 4 to index i + 5 is a palindrome
        substring = string[i-4:i+6]
        if substring == substring[::-1]:
            # If it is a palindrome, add it to the set of palindromes
            palindromes.add(substring)
    
    return palindromes
