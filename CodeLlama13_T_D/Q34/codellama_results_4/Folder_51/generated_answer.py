
def find_original_set(arg1, arg2, ..., arg28):
    result = set()
    for i in range(28):
        result |= locals()['arg%d' % (i + 1)]
    return result
