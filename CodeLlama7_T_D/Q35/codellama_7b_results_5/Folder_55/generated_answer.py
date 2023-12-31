
def remove_repeat_chars(s):
    # Create a dictionary to keep track of characters and their indices
    char_indices = {}
    for i, c in enumerate(s):
        if c not in char_indices:
            char_indices[c] = [i]
        else:
            char_indices[c].append(i)
    # Remove characters that occur more than once between indices 10 and 100
    for c, indices in char_indices.items():
        if len(indices) > 1 and min(indices) >= 10 and max(indices) <= 100:
            s = ''.join([s[:i], s[i+1:]]))
    return s
