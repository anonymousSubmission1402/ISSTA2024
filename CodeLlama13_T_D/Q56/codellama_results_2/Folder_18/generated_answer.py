
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i:j] not in substrings and len(s[i:j]) == 63:
                substrings.append(s[i:j])
    return substrings
