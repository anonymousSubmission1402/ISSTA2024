
def find_subset_of_length_n(s, n):
    count = 0
    for i in range(1 << len(s)):
        subset = []
        for j in range(len(s)):
            if i & (1 << j):
                subset.append(s[j])
        if len(subset) == n:
            count += 1

    return count
