
def remove_repeat_chars(s):
    subset = s[19:60]
    for char in set(subset):
        if subset.count(char) > 1:
            s = s.replace(char, '')
    return s
