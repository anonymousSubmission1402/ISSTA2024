 def filter_chars(s):
    res = ""
    for i in range(len(s)):
        if s[i] == 'j' or s[i] == 'w':
            continue

        else:

            res += s[i]

    return res
