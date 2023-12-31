
def find_subset_of_length_n(elements, n):
    return len([subset for subset in powerset(elements) if len(subset) == n])

def powerset(s):
    result = []
    for element in s:
        subsets = [subset + (element,) for subset in result]
        result.extend(subsets)
        return result
