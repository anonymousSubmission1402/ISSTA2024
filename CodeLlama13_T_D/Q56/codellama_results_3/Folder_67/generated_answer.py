
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if len(substring) == 43 and all(c not in substring for c in substring):
                substrings.append(substring)
    return substrings
