
def remove_repeat_chars(s):
    seen = set()
    out = []
    for c in s:
        if c not in seen and seen.add(c):
            out.append(c)
    return "".join(out)
