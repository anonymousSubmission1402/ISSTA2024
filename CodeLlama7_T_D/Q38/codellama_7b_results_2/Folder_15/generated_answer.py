
def find_subset_of_length_n(set):
    n = len(set)
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(set[j])
        subsets.append(subset)
    return len([s for s in subsets if len(s) == 10])
