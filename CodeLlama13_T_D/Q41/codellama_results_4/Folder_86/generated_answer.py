
def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    result = set()
    for i in range(31, 35):
        for j in range(i+1, 36):
            if list1[i] == list2[j]:
                result.add(list1[i])
    return result
