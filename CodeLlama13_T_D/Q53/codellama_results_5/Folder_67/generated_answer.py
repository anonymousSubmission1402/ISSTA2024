
def palindrome_of_length_at_least_n(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter and not at the end of the string
        if string[i].isalpha() and (i + 1) < len(string):
            # Initialize a variable to store the length of the palindrome
            length = 0
            
            # Loop through each character in the string starting from the current index
            for j in range(i, len(string)):
                # Check if the current character is a letter and not at the end of the string
                if string[j].isalpha() and (j + 1) < len(string):
                    # Increment the length of the palindrome by 2
                    length += 2
                    
                    # Check if the length of the palindrome is greater than or equal to 25
                    if length >= 25:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(string[i:j+1])
                    
                    # Break out of the inner loop if the length of the palindrome is greater than or equal to 25
                    if length >= 25:
                        break
            
    # Return the set of palindromes
    return palindromes
