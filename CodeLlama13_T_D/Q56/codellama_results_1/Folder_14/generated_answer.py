
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 84):
        substring = s[i:i+85]
        if len(set(substring)) == 85 and not any(substring[j] in substring[:j] for j in range(1, 85)):
            substrings.append(substring)
    return substrings
