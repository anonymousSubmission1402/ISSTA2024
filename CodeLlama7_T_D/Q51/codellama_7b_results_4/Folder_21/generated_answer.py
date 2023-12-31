
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Create a set of all the anagrams in the list
    anagram_set = set()
    for word in my_list:
        anagram_set.add("".join(sorted(word))))

    # Check if there are at most 26 pairs of anagrams in the list
    return len(anagram_set) <= 26
