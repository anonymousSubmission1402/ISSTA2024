
def identical_elements(list1, list2):
    result = []
    for i in range(34, 56):
        if list1[i] == list2[i]:
            result.append(list1[i])
    return set(result)
