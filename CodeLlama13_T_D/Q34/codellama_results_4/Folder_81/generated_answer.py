
def find_original_set(sets):
    original_set = set()
    for s in sets:
        if len(s - original_set) == 0:
            continue
        else:
            original_set |= s
    return original_set
