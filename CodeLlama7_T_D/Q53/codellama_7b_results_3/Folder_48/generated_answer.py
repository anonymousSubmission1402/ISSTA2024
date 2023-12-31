
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter (i.e., not a whitespace or punctuation mark)
        if string[i].isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the reverse of the string
            for j in range(len(string)-1, -1, -1):
                # Check if the current character is a letter (i.e., not a whitespace or punctuation mark)
                if string[j].isalpha():
                    # Add the current character to the palindrome
                    palindrome += string[j]
            # Check if the palindrome has a length greater than or equal to 150
            if len(palindrome) >= n:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
