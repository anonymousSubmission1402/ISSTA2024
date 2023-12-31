
def find_subset_of_length_n(elements):
    return len([sub for sub in powerset(elements) if len(sub) == 78])

def powerset(elements):
    result = []
    for element in elements:
        result += [sub + (element,) for sub in powerset(elements - {element})]
    return result or [()]
