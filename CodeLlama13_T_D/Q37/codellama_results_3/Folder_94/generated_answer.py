
def filter_chars(s):
    filtered = []
    for i, c in enumerate(s):
        if i >= 51 and i <= 96 and 'X' <= c <= 'p':
            continue
        filtered.append(c)
    return ''.join(filtered)
