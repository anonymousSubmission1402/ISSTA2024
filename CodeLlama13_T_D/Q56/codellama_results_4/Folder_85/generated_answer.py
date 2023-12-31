
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 13):
        substring = s[i:i+14]
        if len(set(substring)) == 14 and not any(c in substring for c in substrings):
            substrings.append(substring)
    return substrings
