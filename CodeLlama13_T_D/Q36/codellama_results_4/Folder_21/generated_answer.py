
def filter_chars(s):
    result = ""
    for i, c in enumerate(s):
        if (i < 219 or i > 403) and c not in "*7":
            result += c
    return result
