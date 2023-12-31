
def palindromes_of_specific_lengths(string):
    # Define the substring range and length range
    substring_range = range(0, len(string))
    length_range = range(5, 81)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the substring range and length range
    for start in substring_range:
        for length in length_range:
            # Check if the substring is a palindrome
            if is_palindrome(string[start:start+length], ignore_case=True):
                # Add the palindrome to the set
                palindromes.add(string[start:start+length])
    return palindromes

def is_palindrome(string, ignore_case=False):
    if ignore_case:
        string = string.lower()
    return string == string[::-1]
