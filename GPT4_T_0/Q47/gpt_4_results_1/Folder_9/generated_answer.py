
def palindromes_of_specific_lengths(s):
    s = s[:301]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+50, min(i+61, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
