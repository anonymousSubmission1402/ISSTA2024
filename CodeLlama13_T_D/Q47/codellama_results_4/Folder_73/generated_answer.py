
def palindromes_of_specific_lengths(string):
    # Initialize a set to store the palindromes
    palindromes = set()
    
    # Iterate over the string from index 21 to 62, both inclusive
    for i in range(21, 63):
        # Iterate over the length of each substring from 22 to 33 (both inclusive)
        for j in range(22, 34):
            # Check if the substring is a palindrome and consists only of English letters
            if string[i:i+j] == string[i+j-1::-1] and all(c.isalpha() for c in string[i:i+j]):
                # If it is, add it to the set of palindromes
                palindromes.add(string[i:i+j])
    
    # Return the set of palindromes
    return palindromes
