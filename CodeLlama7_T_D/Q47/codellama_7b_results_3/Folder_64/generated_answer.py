 def palindromes_of_specific_lengths(string):
    # Create a list of all substrings within the specified index range
    substrings = []
    for i in range(8):
        substring = string[i:i+8]
        substrings.append(substring)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring and check if it is a palindrome
    for substring in substrings:
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # Add the palindrome to the set
            palindromes.add(substring)
    # Filter the palindromes to only include those with lengths between 4 and 5 (both inclusive)
    filtered_palindromes = {x for x in palindromes if len(x) in range(4, 6)}
    return filtered_palindromes
