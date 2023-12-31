
def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        anagram_set = set()
        for c in s.lower():
            anagram_set.add(c)
        if len(anagram_set) >= 3 and len(list(anagram_set)) > 1:
            anagrams.append((s, list(anagram_set)))
    return len(anagrams) >= 67
