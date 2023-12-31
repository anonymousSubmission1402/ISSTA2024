
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Loop through each substring of the given string
    for i in range(len(string)):
        # Check if the substring is a palindrome
        if string[i:i+92] == string[i:i+92][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(string[i:i+92])

    # Return the set of palindromes
    return palindromes
