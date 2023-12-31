
def return_n_greatest_chars(string):
    char_counts = {}
    for c in string:
        if c not in char_counts:
            char_counts[c] = 1
        else:
            char_counts[c] += 1

    sorted_chars = sorted(char_counts, key=lambda x: -char_counts[x])
    return sorted_chars[:33]
