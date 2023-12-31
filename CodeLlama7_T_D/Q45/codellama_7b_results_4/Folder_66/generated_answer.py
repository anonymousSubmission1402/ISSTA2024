
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each substring of length 5 in the string
    for i in range(len(string) - 4):
        # Extract the substring and convert it to lowercase
        substring = string[i:i+5].lower()
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the substring to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes
