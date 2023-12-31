 def palindrome_of_length_at_least_n(string, n):
    # Create a dictionary to store the palindromes
    palindromes = {}
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter (lowercase or uppercase)
        if char.isalpha():
            # Convert the character to lowercase
            char_low = char.lower()
            # Loop through each character in the string starting from index i + 1
            for j in range(i + 1, len(string)):
                # Get the character at index j
                char2 = string[j]
                # If the character is a letter (lowercase or uppercase)
                if char2.isalpha():
                    # Convert the character to lowercase
                    char2_low = char2.lower()
                    # Check if the characters at indices i and j are the same in lowercase
                    if char_low == char2_low:
                        # If the length of the palindrome is greater than or equal to n
                        if len(string[i:j + 1]) >= n:
                            # Add the palindrome to the dictionary
                            palindromes[string[i:j + 1]] = True
    # Return the set of all palindromes in the given string
    return set(palindromes.keys())
