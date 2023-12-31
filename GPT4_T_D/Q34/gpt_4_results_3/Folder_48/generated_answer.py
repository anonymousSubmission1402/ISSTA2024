
def find_original_set(*args):
    if len(args) != 990:
        raise ValueError("Invalid number of arguments")
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("All arguments must be sets")
        original_set = original_set.union(arg)
    return original_set
