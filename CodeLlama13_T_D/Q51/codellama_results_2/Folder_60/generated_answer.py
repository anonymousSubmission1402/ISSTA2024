
def if_contains_anagrams(list_of_strings):
    anagrams = []
    for s in list_of_strings:
        lower_s = s.lower()
        if len(lower_s) < 3 or lower_s in anagrams:
            continue
        else:
            anagrams.append(lower_s)
    return len(anagrams) <= 77
