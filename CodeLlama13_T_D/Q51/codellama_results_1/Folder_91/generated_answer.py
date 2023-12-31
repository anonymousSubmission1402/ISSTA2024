
def if_contains_anagrams(my_list):
    anagram_pairs = []
    for i in range(len(my_list)):
        str1 = my_list[i].lower()
        for j in range(i+1, len(my_list)):
            str2 = my_list[j].lower()
            if len(str1) >= 3 and len(str2) >= 3:
                anagram = "".join(sorted(str1)) == "".join(sorted(str2))
                if anagram:
                    anagram_pairs.append((str1, str2))
    return len(anagram_pairs) <= 88
