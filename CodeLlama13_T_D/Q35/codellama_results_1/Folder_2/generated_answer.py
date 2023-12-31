
def remove_repeat_chars(s):
    seen = {}
    result = []
    for i, c in enumerate(s):
        if i < 72 or i > 93:
            result.append(c)
        elif c not in seen:
            result.append(c)
            seen[c] = True
    return "".join(result)
