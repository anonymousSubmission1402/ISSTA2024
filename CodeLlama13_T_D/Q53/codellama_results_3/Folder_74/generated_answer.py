
def palindrome_of_length_at_least_n(string, n):
    # Find all substrings of length greater than or equal to 57 that exist in the given string
    substrings = [string[i:j] for i in range(len(string)) for j in range(i+1, len(string)+1)]
    
    # Filter out any substrings that are not palindromes of length greater than or equal to 57
    palindromes = [substring for substring in substrings if substring == substring[::-1]]
    
    return set(palindromes)
