
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                count += 1
                if count > 6:
                    return False
    return True
