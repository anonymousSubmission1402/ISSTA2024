
def palindrome_of_length_at_least_n(string, n=49):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the character to uppercase
            char_upper = string[i].upper()
            # Loop through each character in the rest of the string
            for j in range(i+1, len(string)):
                # Check if the character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Convert the character to uppercase
                    char_lower = string[j].upper()
                    # Check if the two characters form a palindrome of length greater than or equal to n
                    if char_upper == char_lower:
                        # If they do, add them to the set of palindromes
                        palindromes.add((char_upper + char_lower)[::-1])
    # Return the set of palindromes
    return palindromes
