
import itertools

def if_contains_anagrams(strings):
    anagram_pairs = 0

    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1 = strings[i].lower()
            str2 = strings[j].lower()
            
            if sorted(str1) == sorted(str2) and len(str1) >= 3:
                anagram_pairs += 1
                
                if anagram_pairs > 30:
                    return False
    
    return True
