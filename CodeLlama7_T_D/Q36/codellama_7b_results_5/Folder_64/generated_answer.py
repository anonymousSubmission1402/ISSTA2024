
def filter_chars(s):
    new_str = ""
    for i in range(1, len(s)):
        if s[i] > "3" and s[i] < "^":
            continue

        else:

            new_str += s[i]

    return new_str
