
def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    substring = string[23:82].lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substring)):
        # Check if the character is a letter (a-z or A-Z)
        if substring[i].isalpha():
            # Create a new string that is the palindrome
            palindrome = ''

            # Iterate over the characters in the substring from index i to index 23, both inclusive
            for j in range(i, len(substring[:23])):
                # Add the character to the palindrome string
                palindrome += substring[j]

            # Check if the palindrome has a length between 32 and 34 (both inclusive)
            if len(palindrome) >= 32 and len(palindrome) <= 34:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
