
def find_original_set(*args):
    if len(args) != 56:
        raise ValueError('Exactly 56 arguments are required')

    original_set = set()

    for arg in args:
        original_set = original_set.union(arg)

    return original_set
