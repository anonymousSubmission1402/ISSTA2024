
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 84):
        substring = s[i:i+85]
        if len(set(substring)) == 85 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
