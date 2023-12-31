 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(1, len(string) - 3):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the index of the corresponding letter in the reverse of the string
            rev_index = len(string) - i - 1
            # Check if the corresponding letter in the reverse of the string is also a letter
            if string[rev_index].isalpha():
                # Form a palindrome by concatenating the current character with its corresponding letter in the reverse of the string
                palindrome = string[i] + string[rev_index]
                # Check if the formed palindrome has at least 5 letters
                if len(palindrome) >= 5:
                    # Add the formed palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
