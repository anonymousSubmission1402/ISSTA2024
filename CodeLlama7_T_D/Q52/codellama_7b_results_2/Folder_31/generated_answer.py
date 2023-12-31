
def palindrome_of_length_n(string):
    # Remove non-letter characters from the string
    cleaned_string = ''.join([char for char in string if char.isalpha()])

    # Convert the string to lowercase for case-insensitive comparison
    lowercase_cleaned_string = cleaned_string.lower()

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each substring of length n in the cleaned string
    for i in range(len(lowercase_cleaned_string) - 5):
        # Check if the substring is a palindrome
        if lowercase_cleaned_string[i:i+6] == lowercase_cleaned_string[i:i+6][::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(lowercase_cleaned_string[i:i+6])

    # Return the set of palindromes
    return palindromes
