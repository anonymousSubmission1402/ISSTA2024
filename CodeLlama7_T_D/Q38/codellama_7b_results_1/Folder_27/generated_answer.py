
def find_subset_of_length_n(set_elements):
    total_subsets = 0
    for i in range(1 << len(set_elements)):
        subset = []
        for j in range(len(set_elements)):
            if i & (1 << j):
                subset.append(set_elements[j])
        if len(subset) == 56:
            total_subsets += 1
    return total_subsets
