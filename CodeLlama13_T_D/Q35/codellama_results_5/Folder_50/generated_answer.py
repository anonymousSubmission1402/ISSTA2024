
def remove_repeat_chars(s):
    seen = {}
    new_string = ''
    for i in range(13, 76):
        if s[i] not in seen:
            seen[s[i]] = True
            new_string += s[i]
    return new_string
