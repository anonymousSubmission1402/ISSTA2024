
def find_original_set(args):
    sets = list(map(set, args))
    return min(sets, key=len)
