
def filter_chars(string):
    chars = list(string)
    for i in range(46, 68):
        if chars[i].isalpha() and chars[i] < 'H' and chars[i] > 's':
            while True:
                try:
                    chars.remove(chars[i])
                except ValueError:
                    break
    return "".join(chars)
