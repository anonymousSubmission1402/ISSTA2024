
def palindrome_of_length_n(string, n):
    return {s[::-1] for s in string if len(s) == n and s.isalpha()}
