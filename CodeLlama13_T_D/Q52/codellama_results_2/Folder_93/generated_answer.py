
def palindrome_of_length_n(string):
    # Find all substrings of the given string that are palindromes of length 45
    palindromes = []
    for i in range(len(string) - 44):
        substring = string[i:i+45]
        if substring == substring[::-1]:
            palindromes.append(substring)
    
    # Return the set of all palindromes found
    return set(palindromes)
