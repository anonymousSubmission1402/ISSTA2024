
def if_contains_anagrams(my_list):
    pairs = []
    for i in range(len(my_list)):
        word1 = my_list[i].lower()
        for j in range(i + 1, len(my_list)):
            word2 = my_list[j].lower()
            if len(word1) >= 3 and len(word2) >= 3:
                pairs.append((word1, word2))
    return any(len(set(pair)) == 1 for pair in pairs)
