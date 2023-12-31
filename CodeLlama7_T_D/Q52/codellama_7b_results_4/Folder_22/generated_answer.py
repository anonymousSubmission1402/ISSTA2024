
def palindrome_of_length_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the length of the substring starting from the current character
            substr_length = len(string) - i
            # If the substring length is greater than or equal to 20, check for palindromes in the substring
            if substr_length >= 20:
                # Initialize a variable to store the palindrome
                palindrome = ""
                # Loop through each character in the substring
                for j in range(substr_length):
                    # Check if the current character is a letter and it is not the first or last character in the substring
                    if string[i + j].isalpha() and (j == 0 or j == substr_length - 1):
                        # Add the palindrome to the set of palindromes
                        palindromes.add(palindrome)
                        # Break out of the loop since we have found a palindrome
                        break

                # If there are any palindromes in the substring, add them to the set of palindromes
                if len(palindromes) > 0:
                    # Return the set of palindromes
                    return palindromes
