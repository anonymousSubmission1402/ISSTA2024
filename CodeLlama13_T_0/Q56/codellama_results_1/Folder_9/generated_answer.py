
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 34 + 1):
        substring = s[i:i+34]
        if len(set(substring)) == 34 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
