
from math import comb

def find_subset_of_length_n(elements):
    if len(elements) < 312:
        return 0
    return comb(len(elements), 312)
