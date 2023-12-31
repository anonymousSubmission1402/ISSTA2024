
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if j - i == 110:
                substring = s[i:j]
                if all_distinct_chars(substring) and substring not in substrings:
                    substrings.append(substring)
    return substrings

def all_distinct_chars(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        else:
            seen.add(c)
    return True
