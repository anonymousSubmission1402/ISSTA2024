def find_original_set(s):
    return set(min(s, key=lambda x: x))
