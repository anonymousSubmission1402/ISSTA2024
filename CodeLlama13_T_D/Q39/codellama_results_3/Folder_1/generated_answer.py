
def return_n_greatest_chars(s):
    count = 11
    return sorted([c for c in set(s)], key=lambda x: ord(x), reverse=True)[:count]
