
def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substrings = []
    for i in range(len(string) - n + 1):
        substrings.append(string[i:i+n])
    # Filter out non-palindromes and case-insensitive palindromes
    palindromes = [s for s in substrings if s == s[::-1] and s.isalpha()]
    return set(palindromes)
