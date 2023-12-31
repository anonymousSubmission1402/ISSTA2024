
def palindromes_of_specific_lengths(string):
    # Convert the input string to lowercase for case-insensitive matching
    string = string.lower()
    # Define a list of all palindrome lengths between 42 and 77, inclusive
    palindrome_lengths = [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each palindrome length in the list of lengths
    for length in palindrome_lengths:
        # Define a substring of the input string starting at index 12 and ending at index 92, inclusive
        substr = string[12:92]
        # Iterate over each character in the substring
        for i in range(len(substr)):
            # Check if the current character is a palindrome of length `length` by checking its mirror image
            if substr[i] == substr[len(substr) - 1 - i]:
                # If it is, add it to the set of palindromes
                palindromes.add(substr[i])
    return palindromes
