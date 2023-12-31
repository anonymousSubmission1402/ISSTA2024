
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        substr = string[i:]
        if len(substr) >= 62 and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
