 def filter_chars(s):
    filtered = ""
    for i, c in enumerate(s):
        if (503 <= i <= 753) and ('9' <= c <= 'w'):
            continue

        filtered += c

    return filtered
