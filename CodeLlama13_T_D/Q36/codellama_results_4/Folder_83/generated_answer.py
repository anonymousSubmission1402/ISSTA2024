
def filter_chars(s):
    result = ""
    for i, c in enumerate(s):
        if i < 72 or i > 93:
            result += c
        elif c > "<" and c < "J":
            continue
        else:
            result += c
    return result
