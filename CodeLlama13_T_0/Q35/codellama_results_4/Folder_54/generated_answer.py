
def remove_repeat_chars(s):
    seen = set()
    result = []
    for i, c in enumerate(s[35:64]):
        if c not in seen and i < 64:
            result.append(c)
            seen.add(c)
    return "".join(result) + s[64:]
