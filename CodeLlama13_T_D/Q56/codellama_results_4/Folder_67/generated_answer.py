
def all_substring_of_size_n(s, n):
    subs = []
    for i in range(len(s) - n + 1):
        sub = s[i:i+n]
        if not any(sub in s[:i] or sub in s[i+n:] for sub in subs):
            subs.append(sub)
    return subs
