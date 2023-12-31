
def if_contains_anagrams(my_list):
    # Check if there are at most 42 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_pairs += 1
                if num_pairs > 42:
                    return False

    # Check if there are at least three anagrams in the list

    for i in range(len(my_list)):
        count = 0
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                count += 1
                if count >= 3:
                    return True

    # If there are no anagrams in the list, return False

    return False
