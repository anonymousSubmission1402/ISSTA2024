
def if_contains_anagrams(str_list):
    # Count the number of pairs of anagrams in the list
    anagram_count = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                anagram_count += 1
    # Return True if there are at least 85 pairs of anagrams in the list, otherwise False
    return anagram_count >= 85
