
def return_n_greatest_chars(string):
    chars = sorted(set(string), reverse=True)
    return chars[:23]
