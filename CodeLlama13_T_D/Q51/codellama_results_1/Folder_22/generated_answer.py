
def if_contains_anagrams(strlist):
    for i in range(len(strlist)):
        if len(strlist[i]) < 3:
            continue
        ana1 = ''.join(sorted(strlist[i].lower()))
        for j in range(i+1, len(strlist)):
            if len(strlist[j]) < 3:
                continue
            ana2 = ''.join(sorted(strlist[j].lower()))
            if ana1 == ana2:
                return True
    return False
