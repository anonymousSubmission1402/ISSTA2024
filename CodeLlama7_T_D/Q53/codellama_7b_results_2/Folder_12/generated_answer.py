
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the character is a letter (not a space or punctuation)
        if string[i].isalpha():
            # Loop through each character in the string starting from the current index and moving forward
            for j in range(i + 1, len(string) + 1):
                # Check if the substring is a palindrome (same when read forward or backward)
                if string[i:j] == string[i:j][::-1]:
                    # Add the palindrome to the set
                    palindromes.add(string[i:j])
    # Return the set of palindromes
    return palindromes
