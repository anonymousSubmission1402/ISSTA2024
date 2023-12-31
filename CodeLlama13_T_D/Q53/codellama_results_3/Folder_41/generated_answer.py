
def palindrome_of_length_at_least_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each substring of length greater than or equal to 28 in the given string
    for i in range(len(string) - 27):
        # Check if the substring is a palindrome
        if string[i:i+28] == string[i:i+28][::-1]:
            # Add the palindrome to the set
            palindromes.add(string[i:i+28])
    
    return palindromes
