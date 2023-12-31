 def palindromes_of_specific_lengths(string):
    # Define the index range for searching palindromes
    start_index = 127
    end_index = 288
    # Create an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(start_index, end_index + 1):
        # Check if the character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Define the length of the palindrome
            palindrome_length = 141 - 119 + 1
            # Create an empty string to store the palindrome
            palindrome = ""
            # Loop through each character in the palindrome
            for j in range(i, i + palindrome_length):
                # Check if the character is a letter (a-z or A-Z)
                if string[j].isalpha():
                    # Add the character to the palindrome
                    palindrome += string[j]
            # Check if the palindrome is valid
            if len(palindrome) == 141 - 119 + 1 and palindrome.lower() == palindrome:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
