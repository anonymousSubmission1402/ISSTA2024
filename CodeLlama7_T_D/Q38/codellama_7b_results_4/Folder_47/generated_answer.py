
def find_subset_of_length_n(set):
    subset_count = 0
    for i in range(len(set)):
        for j in range(i + 1, len(set)):
            if len({set[i], set[j]}) == n:
                subset_count += 1

    return subset_count
