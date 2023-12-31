
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i, len(s) - 91):
            substring = s[i:j+92]
            if not any(c in substring for c in substrings):
                substrings.append(substring)
    return substrings
