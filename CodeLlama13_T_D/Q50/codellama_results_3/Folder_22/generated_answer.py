
def if_contains_anagrams(list_of_strings):
    pairs = 0
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            if sorted(list_of_strings[i].lower()) == sorted(list_of_strings[j].lower()):
                pairs += 1
    return pairs >= 72
