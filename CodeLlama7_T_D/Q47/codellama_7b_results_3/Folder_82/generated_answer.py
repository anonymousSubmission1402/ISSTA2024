
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, 301):
        # Check if there is a palindrome of length i in the substring
        if string[3:301].find(string[3:301][::-1]) != -1:
            # If there is a palindrome, add it to the set of palindromes
            palindromes.add(string[3:301][::-1])
    return palindromes
