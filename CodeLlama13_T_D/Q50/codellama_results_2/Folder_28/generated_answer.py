
def if_contains_anagrams(strings):
    for i in range(len(strings)):
        str1 = strings[i].lower()
        for j in range(i + 1, len(strings)):
            str2 = strings[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                if "".join(sorted(str1)) == "".join(sorted(str2)):
                    return True
    return False
