
def if_contains_anagrams(strings):
    anagrams = []
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            s1 = strings[i].lower()
            s2 = strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                ss1 = ''.join(sorted(s1))
                ss2 = ''.join(sorted(s2))
                if ss1 == ss2 and [ss1, ss2] not in anagrams:
                    anagrams.append([ss1, ss2])
    return len(anagrams) <= 206
