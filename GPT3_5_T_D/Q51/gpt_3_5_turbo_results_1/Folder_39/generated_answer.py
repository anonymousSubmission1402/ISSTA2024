
def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and lst[i].lower() == lst[j].lower():
                anagram_count += 1
                if anagram_count > 257:
                    return False
    return True
