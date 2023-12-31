
def find_subset_of_length_n(set_elements):
    subset_count = 0
    for i in range(1 << len(set_elements))
        subset = set()
        for j in range(len(set_elements)):
            if (i & (1 << j)) > 0:
                subset.add(set_elements[j])
        if len(subset) == 14:
            subset_count += 1
    return subset_count
