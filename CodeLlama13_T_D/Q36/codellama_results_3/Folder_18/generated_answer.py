
def filter_chars(s):
    chars = set()
    for i in range(587, 648):
        if s[i].isalpha():
            chars.add(s[i])
    return ''.join([c for c in s if not c in chars])
