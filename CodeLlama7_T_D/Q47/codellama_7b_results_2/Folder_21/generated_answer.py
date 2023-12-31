
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the specified index range
    palindromes = []
    for i in range(100, 296):
        sub_string = string[i - 100:i]
        # Check if the substring is a palindrome
        if sub_string == sub_string[::-1]:
            # Add the palindrome to the list
            palindromes.append(sub_string)
    # Filter the palindromes based on their length
    filtered_palindromes = []
    for palindrome in palindromes:
        if 136 <= len(palindrome) <= 160:
            filtered_palindromes.append(palindrome)
    # Return the set of filtered palindromes
    return set(filtered_palindromes)
