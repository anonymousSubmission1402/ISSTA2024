 def filter_chars(s):
    for i in range(672, 709):
        if s[i] > 'X' and s[i] < '}':
            s = s[:i] + s[i+1:]
    return s
