
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    start = 200
    end = 300
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = min(end - i + 1, 50)
            # Iterate over the possible lengths of the palindrome
            for j in range(10, length + 1):
                # Check if the substring from index i to index i + j is a palindrome
                if string[i:i+j] == string[i:i+j][::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[i:i+j])
    # Return the set of palindromes found in the specified index range
    return palindromes
