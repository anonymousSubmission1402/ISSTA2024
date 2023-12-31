
def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive search
    string = string.lower()
    # Create an empty set to store the palindromes
    palindromes = set()
    # Iterate through each substring of length n in the given string
    for i in range(len(string) - 2):
        # Extract a substring of length n from the current position in the string
        substring = string[i:i+3]
        # Check if the substring is a palindrome by comparing it to its reverse
        if substring == substring[::-1]:
            # If the substring is a palindrome, add it to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes found in the given string
    return palindromes
