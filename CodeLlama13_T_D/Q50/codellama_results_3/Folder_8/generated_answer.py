
def if_contains_anagrams(my_list):
    anagram_count = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i].lower() == my_list[j].lower():
                continue
            else:
                anagram = "".join(sorted(my_list[i]))
                anagram2 = "".join(sorted(my_list[j]))
                if anagram == anagram2 and len(anagram) >= 3:
                    anagram_count += 1
        if anagram_count >= 85:
            return True
        else:
            return False
