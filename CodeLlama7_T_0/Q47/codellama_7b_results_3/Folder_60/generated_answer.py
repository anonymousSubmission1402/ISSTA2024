
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    start = 23
    end = 82
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = 32

            # Iterate over the characters in the substring from index i to index i + length - 1
            for j in range(i, i + length):
                # Check if the character at index j is a letter
                if string[j].isalpha():
                    # Define the palindrome as the substring from index i to index j
                    palindrome = string[i:j]
                    # Check if the palindrome is case-insensitive and only consists of English letters
                    if palindrome.lower() == palindrome and palindrome.isalpha():
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
