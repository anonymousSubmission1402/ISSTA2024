
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        key = "".join(sorted(s.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams.add(key)
            if len(anagrams) > 16:
                return False
    return True
