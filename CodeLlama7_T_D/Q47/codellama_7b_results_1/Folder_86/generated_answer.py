
def palindromes_of_specific_lengths(string):
    # Define the substring range
    start = 30
    end = 95
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the substring
    for i in range(start, end + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Initialize an empty string to store the current palindrome
            palindrome = ""
            # Iterate through each character in the substring from the current index to the end of the substring
            for j in range(i, end + 1):
                # Check if the current character is a letter
                if string[j].isalpha():
                    # Add the current character to the palindrome string
                    palindrome += string[j]
                # Check if the length of the palindrome string is between 34 and 55 (both inclusive)
                if len(palindrome) >= 34 and len(palindrome) <= 55:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return {x.lower() for x in palindromes}
