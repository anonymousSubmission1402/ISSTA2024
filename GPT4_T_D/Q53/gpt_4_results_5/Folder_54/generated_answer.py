
def palindrome_of_length_at_least_n(s):
    s = ''.join(ch.lower() for ch in s if ch.isalpha())
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+74, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
