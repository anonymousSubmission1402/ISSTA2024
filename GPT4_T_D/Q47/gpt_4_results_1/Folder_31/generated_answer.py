
def palindromes_of_specific_lengths(s):
    import re
    s = s[11:84]
    s = re.sub('[^a-zA-Z]+', '', s)
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i+37, min(i+61, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                results.add(substring)
    return results
