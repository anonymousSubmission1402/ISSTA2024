
def find_subset_of_length_n(elements, n):
    subsets = []
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            for k in range(j+1, len(elements)):
                if elements[i] + elements[j] + elements[k] == n:
                    subsets.append([elements[i], elements[j], elements[k]])
    return subsets
