
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s in strings:
        for t in range(len(s)-1, len(s)-4):
            for i in range(t+1, len(s)):
                if sorted(s[t:i]) == sorted(s[i:i+3]):
                    anagram_pairs += 1
                    break
        if anagram_pairs > 475:
            return False
    return True
