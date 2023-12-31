
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(my_list) - 1)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_anagrams += 1
    # Check if there are at least 58 pairs of anagrams in the list
    return num_anagrams >= 58
