
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Convert the character to lowercase
            char = string[i].lower()
            # Loop through each character in the reversed string
            for j in range(len(string)-1, -1, -1):
                # Check if the character is a letter (a-z or A-Z)
                if string[j].isalpha():
                    # Convert the character to lowercase
                    rev_char = string[j].lower()
                    # Check if the character and its reverse are the same
                    if char == rev_char:
                        # If the length of the palindrome is greater than or equal to n, add it to the set of palindromes
                        if len(string[i:j+1]) >= n:
                            palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
