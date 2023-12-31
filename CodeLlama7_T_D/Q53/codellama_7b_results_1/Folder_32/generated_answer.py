
def palindrome_of_length_at_least_n(string, n):
    # Split the string into individual characters
    chars = [char for char in string]
    # Create a set to store all palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(len(chars)):
        # Check if the current character is a letter
        if chars[i].isalpha():
            # Create a copy of the string without the current character
            temp_string = ''.join(chars[:i]) + ''.join(chars[i+1:])
            # Check if the temporary string is a palindrome
            if temp_string == temp_string[::-1]:
                # Add the temporary string to the set of palindromes
                palindromes.add(temp_string)
    return palindromes
