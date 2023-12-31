
def palindromes_of_specific_lengths(string):
    # Define the index range for considering palindromes
    start_index = 0
    end_index = 9
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string within the specified index range
    for i in range(start_index, end_index + 1):
        # Define the substring of length 3 to 5 that contains the current character
        substring = string[i - 2:i + 1]
        # Check if the substring is a palindrome and its length falls within the specified range
        if substring == substring[::-1] and len(substring) in range(3, 6):
            # Add the palindrome to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes found within the specified index range
    return palindromes
