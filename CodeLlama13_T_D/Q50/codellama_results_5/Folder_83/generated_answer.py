
def if_contains_anagrams(str_list):
    pairs = 0
    for s1 in str_list:
        for s2 in str_list:
            if len(s1) >= 3 and len(s2) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                pairs += 1
                if pairs >= 48:
                    return True
    return False
