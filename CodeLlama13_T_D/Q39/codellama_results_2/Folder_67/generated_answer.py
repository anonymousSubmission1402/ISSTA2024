
def return_n_greatest_chars(s):
    n = 66
    return sorted(s, key=lambda x: ord(x), reverse=True)[:n]
