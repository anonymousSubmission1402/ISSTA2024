
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is a letter (uppercase or lowercase)
        if char.isalpha():
            # Convert the character to uppercase
            char_upper = char.upper()
            # Loop through each character in the string starting from index i + 1
            for j in range(i + 1, len(string)):
                # Get the character at index j
                char2 = string[j]
                # If the character is a letter (uppercase or lowercase)
                if char2.isalpha():
                    # Convert the character to uppercase
                    char2_upper = char2.upper()
                    # Check if the characters at index i and index j are the same in uppercase
                    if char_upper == char2_upper:
                        # If the length of the substring starting from index i and ending at index j is greater than or equal to n, add it to the set of palindromes
                        if len(string[i:j + 1]) >= n:
                            palindromes.add(string[i:j + 1])
    # Return the set of palindromes
    return palindromes
