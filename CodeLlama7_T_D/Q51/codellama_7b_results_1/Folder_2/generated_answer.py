
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    anagram_count = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                anagram_count += 1
    # Return True if there are at most 81 pairs of anagrams in the list, and False otherwise.
    return anagram_count <= 81
