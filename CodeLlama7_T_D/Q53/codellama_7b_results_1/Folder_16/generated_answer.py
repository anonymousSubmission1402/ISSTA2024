 def palindrome_of_length_at_least_n(string, n):
    # Convert the input string to lowercase
    string = string.lower()
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(string)):
        # Get the substring starting at index i and ending at the end of the string
        substr = string[i:]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substr)
    # Return the set of palindromes with length greater than or equal to n
    return {p for p in palindromes if len(p) >= n}
