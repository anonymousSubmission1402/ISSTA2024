
def palindrome_of_length_at_least_n(s):
    import re
    s = re.sub(r'\W+', '', s).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 40, length + 1):
            subs = s[i:j]
            if subs == subs[::-1]:
                palindromes.add(subs)
    return palindromes
