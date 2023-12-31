
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, 9 + 1):
        # Check if the character is a letter
        if string[i].isalpha():
            # Create a palindrome by concatenating the character with its reverse
            palindrome = string[i] + string[i][::-1]
            # Add the palindrome to the set of palindromes
            palindromes.add(palindrome)
    return palindromes
