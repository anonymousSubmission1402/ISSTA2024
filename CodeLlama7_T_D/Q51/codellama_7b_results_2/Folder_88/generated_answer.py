
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize a set to store the anagram pairs
    anagram_pairs = set()

    # Iterate over the list of strings
    for s1 in my_list:

        # Iterate over the rest of the list of strings
        for s2 in my_list[my_list.index(s1) + 1:]:

            # If the two strings are anagrams, add them to the set
            if sorted(s1) == sorted(s2):
                anagram_pairs.add((s1, s2))

    # Return True if there are at most 407 pairs of anagrams in the list
    return len(anagram_pairs) <= 407
