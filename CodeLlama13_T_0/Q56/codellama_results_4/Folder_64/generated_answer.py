
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 7):
        substring = s[i:i+8]
        if len(set(substring)) == 8 and not any(substring in sub for sub in substrings):
            substrings.append(substring)
    return substrings
