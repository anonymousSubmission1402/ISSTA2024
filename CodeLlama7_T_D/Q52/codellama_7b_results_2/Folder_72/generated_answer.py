
def palindrome_of_length_n(string):
    # Define the set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string
    for i in range(len(string)):
        # Check if the character at position i is a letter
        if string[i].isalpha():
            # Get the substring starting from position i and ending at the end of the string
            substr = string[i:].lower()
            # Iterate over the characters in the substring
            for j in range(len(substr)):
                # Check if the character at position j is a letter
                if substr[j].isalpha():
                    # Get the substring starting from the beginning of the string and ending at position j
                    palindrome = string[:j+1].lower()
                    # Add the palindrome to the set
                    palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
