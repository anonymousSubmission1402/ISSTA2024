 def palindromes_of_specific_lengths(string):
    # Define the required substring and its length
    substring = string[11:96]
    substring_length = len(substring)

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the substring
    for i in range(substring_length):
        # Check if the character is a letter
        if substring[i].isalpha():
            # Iterate over the remaining characters in the substring
            for j in range(i + 1, substring_length + 1):
                # Check if the substring from index i to index j is a palindrome
                if substring[i:j] == substring[i:j][::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substring[i:j])

    # Return the set of palindromes that meet the specified requirements
    return palindromes
