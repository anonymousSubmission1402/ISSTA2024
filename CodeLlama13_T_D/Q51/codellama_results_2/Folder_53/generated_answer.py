
def if_contains_anagrams(strlist):
    return len([1 for i in range(len(strlist)) for j in range(i+1, len(strlist)) if sorted(strlist[i].lower()) == sorted(strlist[j].lower()) and len(strlist[i]) >= 3]) <= 8
