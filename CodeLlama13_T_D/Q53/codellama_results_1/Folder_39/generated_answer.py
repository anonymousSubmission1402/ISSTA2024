
def palindrome_of_length_at_least_n(s):
    return {p for p in find_all_palindromes(s) if len(p) >= 69}

def find_all_palindromes(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
