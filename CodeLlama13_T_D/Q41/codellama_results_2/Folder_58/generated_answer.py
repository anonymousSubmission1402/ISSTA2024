
def identical_elements(list1, list2):
    return {element for element in set(list1[209:556]) & set(list2[209:556])}
