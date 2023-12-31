
def palindromes_of_specific_lengths(string):
    # Get the substring of interest
    substring = string[15:89]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its index
        char = substring[i]
        index = i

        # Check if the current character is a letter
        if char.isalpha():
            # Get the reverse of the current character
            reverse_char = char[::-1]
            # Check if the reverse of the current character is a palindrome
            if reverse_char == char:
                # Initialize an empty string to store the palindrome
                palindrome = ""

                # Append the current character and its reverse to the palindrome
                for j in range(index + 1):
                    palindrome += substring[j]

                # Check if the length of the palindrome is between 40 and 72 (both inclusive)
                if len(palindrome) >= 40 and len(palindrome) <= 72:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
