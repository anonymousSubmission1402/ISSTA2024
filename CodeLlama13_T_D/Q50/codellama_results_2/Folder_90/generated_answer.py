
def if_contains_anagrams(list_of_strings):
    count = 0
    for i in range(len(list_of_strings)):
        for j in range(i+1, len(list_of_strings)):
            s1 = list_of_strings[i].lower()
            s2 = list_of_strings[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1) == sorted(s2):
                    count += 1
    return count >= 177
