
def if_contains_anagrams(my_list):
    # Check if there are at least 43 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            # Check if the two strings are anagrams
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                num_pairs += 1
                if num_pairs >= 43:
                    return True
    return False
