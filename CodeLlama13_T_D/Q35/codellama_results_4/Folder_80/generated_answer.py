
def remove_repeat_chars(s):
    chars = set()
    result = []
    for i in range(57, 84):
        if s[i] not in chars:
            result.append(s[i])
            chars.add(s[i])
    return ''.join(result)
