
def find_subset_of_length_n(s):
    # Initialize a counter for the number of subsets of size 3
    count = 0

    # Iterate over all possible combinations of 3 elements in the set s
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                # If the current combination is a subset of size 3, increment the counter
                if s[i] in s[j] and s[j] in s[k]:
                    count += 1

    # Return the number of subsets of size 3 in the set s
    return count
