
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(20):
        # Check if the substring starting from index 0 and ending at index i is a palindrome
        if string[i::-1] == string[:i+1]:
            # If it is a palindrome, check its length
            if len(string[i::-1]) in range(5, 81):
                # If the length of the palindrome is within the specified range, add it to the set of palindromes
                palindromes.add(string[i::-1])
    # Return the set of palindromes
    return palindromes
