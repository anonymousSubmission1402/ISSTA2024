 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the character at index i
        char = string[i]
        # If the character is not uppercase, convert it to uppercase
        if char.islower():
            char = char.upper()
        # Loop through each character in the string from index i + 1 to index len(string) - 1 (exclusive)
        for j in range(i + 1, len(string)):
            # Get the character at index j
            other_char = string[j]
            # If the other character is not uppercase, convert it to uppercase
            if other_char.islower():
                other_char = other_char.upper()
            # If the character and the other character are both uppercase and they are the same, add the palindrome formed by the concatenation of the character and the other character to the set of palindromes
            if char == other_char:
                palindromes.add(char + other_char)
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
