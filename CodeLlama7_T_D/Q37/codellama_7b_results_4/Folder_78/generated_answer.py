 def filter_chars(s):
    new_str = ""
    for i in range(75, 100):
        if s[i] >= '8' and s[i] <= 'e':
            continue

        else:

            new_str += s[i]

    return new_str
