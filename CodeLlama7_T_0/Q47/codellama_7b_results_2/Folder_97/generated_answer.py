
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start_index = 28
    end_index = 94

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = end_index - start_index + 1

            # Iterate over the possible lengths of the palindrome
            for j in range(38, 49 + 1):
                # Check if the length is within the specified range
                if j == length:
                    # Define the substring that forms the palindrome
                    palindrome = string[i - (length // 2) - 1 : i + (length // 2)]

                    # Check if the palindrome is a case-insensitive match for the original string
                    if palindrome.lower() == string.lower():
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
