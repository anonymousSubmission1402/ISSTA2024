
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if j-i == 100:
                substring = s[i:j]
                if not any(substring in s[:i] or substring in s[j:] for i in range(len(s))):
                    substrings.append(substring)
    return substrings
